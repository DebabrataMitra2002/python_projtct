package haldia.hit.compass.core.main

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import haldia.hit.compass.core.util.MyService

class ActivitesViewModel: ViewModel() {

    private val TAG = "ActivitesViewModel"
    val activitesData: LiveData<List<String>> = MyService.test

}