package haldia.hit.compass.core.main

import android.util.Log
import haldia.hit.compass.core.data.PlugsApi
import haldia.hit.compass.core.data.model.Plugs
import haldia.hit.compass.core.util.Resource
import javax.inject.Inject


class DefaultMainRepository @Inject constructor(
    private val api: PlugsApi
) : MainRepository {
    override suspend fun getAverageActivity(): Resource<Plugs> {
        return try {
            val res = api.getAverageActivity()
            val result = res.body()
            Log.d("InsideDMR", res.toString() )
            if (res.isSuccessful && result != null) {
                Resource.Success(result)
            } else {
                Resource.Error(res.message())
            }
        } catch (e: Exception) {
            Resource.Error(e.message ?: "Error Occurred")
        }
    }


}