package haldia.hit.compass.core.di

import com.hivemq.client.mqtt.mqtt5.Mqtt5AsyncClient
import com.hivemq.client.mqtt.mqtt5.Mqtt5Client
import haldia.hit.compass.core.data.PlugsApi
import haldia.hit.compass.core.main.DefaultMainRepository
import haldia.hit.compass.core.main.MainRepository
import haldia.hit.compass.core.util.DispatcherProvider
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import kotlinx.coroutines.CoroutineDispatcher
import kotlinx.coroutines.Dispatchers
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import javax.inject.Singleton


// private const val BASE_URL = "https://iot-hit-test.onrender.com/"
private const val BASE_URL = "http://192.168.1.9:8000/"
private const val MQTT_BROKER_HOST = "192.168.1.9"

@Module
@InstallIn(SingletonComponent::class)
object AppModule {

    @Singleton
    @Provides
    fun providePlugsApi(): PlugsApi = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .addConverterFactory(GsonConverterFactory.create())
        .build()
        .create(PlugsApi::class.java)

    @Singleton
    @Provides
    fun providesMainRepository(api: PlugsApi): MainRepository = DefaultMainRepository(api)


    @Singleton
    @Provides
    fun provideMqttClient(): Mqtt5AsyncClient {
        return Mqtt5Client.builder()
            .identifier("android-client")
            .serverHost(MQTT_BROKER_HOST)
            .buildAsync()
    }


    @Singleton
    @Provides
    fun providesDispatchers(): DispatcherProvider = object : DispatcherProvider {
        override val main: CoroutineDispatcher
            get() = Dispatchers.Main
        override val io: CoroutineDispatcher
            get() = Dispatchers.IO
        override val default: CoroutineDispatcher
            get() = Dispatchers.Default
        override val unconfined: CoroutineDispatcher
            get() = Dispatchers.Unconfined

    }

}