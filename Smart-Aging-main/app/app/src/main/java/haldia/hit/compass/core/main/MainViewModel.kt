package haldia.hit.compass.core.main

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import haldia.hit.compass.core.data.model.Plugs
import haldia.hit.compass.core.main.MainRepository
import haldia.hit.compass.core.util.DispatcherProvider
import haldia.hit.compass.core.util.Resource
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class MainViewModel @Inject constructor(
    private val repository: MainRepository,
    private val dispatcher: DispatcherProvider
) : ViewModel() {

    sealed class PlugsAverageEvent {
        class Success(val successData: Plugs) : PlugsAverageEvent()
        class Failure(val errorText: String) : PlugsAverageEvent()
        object Loading : PlugsAverageEvent()
        object Empty : PlugsAverageEvent()
    }

    private val _plugsAverageData = MutableStateFlow<PlugsAverageEvent>(PlugsAverageEvent.Empty)
    val plugsAverageData: StateFlow<PlugsAverageEvent> = _plugsAverageData

    fun getPlugsAverageData(
    ) {

        viewModelScope.launch(dispatcher.io) {
            _plugsAverageData.value = PlugsAverageEvent.Loading


            when (val ratesResponse = repository.getAverageActivity()) {
                is Resource.Error -> {
                    _plugsAverageData.value =
                        PlugsAverageEvent.Failure(ratesResponse.message.toString())
                }

                is Resource.Success -> {

                    Log.d("InsideVM", ratesResponse.data.toString() )

                    if (ratesResponse.data == null) {
                        _plugsAverageData.value = PlugsAverageEvent.Empty
                    } else {
                        _plugsAverageData.value = PlugsAverageEvent.Success(
                            ratesResponse.data
                        )
                    }
                }
            }
        }

    }
}