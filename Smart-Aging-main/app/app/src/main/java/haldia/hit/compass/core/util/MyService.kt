package haldia.hit.compass.core.util

import android.Manifest
import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.app.Service
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.os.IBinder
import android.util.Log
import androidx.core.app.ActivityCompat
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import androidx.lifecycle.MutableLiveData
import com.hivemq.client.mqtt.datatypes.MqttQos
import com.hivemq.client.mqtt.mqtt5.Mqtt5AsyncClient
import com.hivemq.client.mqtt.mqtt5.Mqtt5Client
import dagger.hilt.android.AndroidEntryPoint
import haldia.hit.compass.MainActivity
import haldia.hit.compass.R
import javax.inject.Inject

@AndroidEntryPoint
class MyService: Service() {

    @Inject
    lateinit var client: Mqtt5AsyncClient

    val CHANNEL_ID = "ForegroundServiceChannel"

    companion object {
        val test = MutableLiveData<List<String>>()
        private val TAG = "AndroidMqttClient"
    }


    override fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int {
        val input = intent.getStringExtra("inputExtra")
        createNotificationChannel()
        val notificationIntent = Intent(this, MainActivity::class.java)
        val pendingIntent = PendingIntent.getActivity(
            this,
            0, notificationIntent, PendingIntent.FLAG_IMMUTABLE
        )
        val notification: Notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("Foreground Service")
            .setContentText(input)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setContentIntent(pendingIntent)
            .build()
        startForeground(1, notification)
        //do heavy work on a background thread
        //stopSelf();


        try {
            client.connect()
                .whenComplete { connAck, throwable ->
                    if (throwable != null) {
                        // Handle failure to connect
                        printMessage("Failed to connect", throwable)
                    } else {
                        // Handle successful connection, e.g. logging or incrementing a metric
                        printMessage("Successfully connected")
                    }
                }

            client.toAsync().subscribeWith()
                .addSubscription().topicFilter("trigger_event").qos(MqttQos.AT_LEAST_ONCE).applySubscription()
                .addSubscription().topicFilter("sensor_data").qos(MqttQos.AT_LEAST_ONCE).applySubscription()
                .callback { publish ->
                    // Handle the received message
                    printMessage(publish.payloadAsBytes.toString(Charsets.UTF_8))
                }
                .send()
                .whenComplete { subAck, throwable ->
                    if (throwable != null) {
                        // Handle failure to subscribe
                        printMessage("Failed to subscribe", throwable)
                    } else {
                        // Handle successful subscription, e.g. logging or incrementing a metric
                        printMessage("Successfully subscribed")
                    }
                }
        } catch (e: Exception) {
            printMessage("Failed to connect", e)
        }

        return START_NOT_STICKY
    }


    private fun printMessage(message: String, throwable: Throwable? = null) {
        test.postValue(
            test.value?.plus(message) ?: listOf(message)
        )
        sendNotification("Trigger Event", message)
        Log.d(TAG, message, throwable)
    }

    fun sendNotification(topic: String, message: String) {
        // sends android native notification, once message is received

        val CHANNEL_ID = "trigger_event"

        var builder = NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setContentTitle(topic)
            .setContentText(message)
            .setSilent(true)
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)

        val name = "TRIGGER EVENT"
        val descriptionText = "Sends a notification when a trigger event is received"
        val importance = NotificationManager.IMPORTANCE_DEFAULT

        val channel = NotificationChannel(CHANNEL_ID, name, importance).apply {
            description = descriptionText
        }

        // Register the channel with the system
        val notificationManager: NotificationManager =
            getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        notificationManager.createNotificationChannel(channel)

        with(NotificationManagerCompat.from(this)) {
            if (ActivityCompat.checkSelfPermission(
                    baseContext,
                    Manifest.permission.POST_NOTIFICATIONS
                ) != PackageManager.PERMISSION_GRANTED
            ) {
                return
            }
            notify(0, builder.build())
        }

    }


    override fun onBind(intent: Intent?): IBinder? {
        return null
    }

    private fun createNotificationChannel() {
        val serviceChannel = NotificationChannel(
            CHANNEL_ID,
            "Foreground Service Channel",
            NotificationManager.IMPORTANCE_DEFAULT
        )
        val manager = getSystemService(
            NotificationManager::class.java
        )
        manager.createNotificationChannel(serviceChannel)
    }

}