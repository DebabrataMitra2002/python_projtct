package haldia.hit.compass.core.main

import haldia.hit.compass.core.data.model.Plugs
import haldia.hit.compass.core.util.Resource


interface MainRepository {

    suspend fun getAverageActivity(): Resource<Plugs>


}