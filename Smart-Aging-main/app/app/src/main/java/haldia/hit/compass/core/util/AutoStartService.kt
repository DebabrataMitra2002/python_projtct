package haldia.hit.compass.core.util

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent

class AutoStartService: BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        val i = Intent(context, MyService::class.java)
        context.startForegroundService(i)
    }
}