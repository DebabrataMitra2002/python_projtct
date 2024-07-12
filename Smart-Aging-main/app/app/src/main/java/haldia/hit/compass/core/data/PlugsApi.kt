package haldia.hit.compass.core.data

import haldia.hit.compass.core.data.model.Plugs
import retrofit2.Response
import retrofit2.http.GET

interface PlugsApi {
    @GET("api/type")
    suspend fun getAverageActivity(): Response<Plugs>

}