package haldia.hit.compass.core.ui.screens

import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.livedata.observeAsState
import androidx.navigation.NavController
import haldia.hit.compass.core.main.ActivitesViewModel


@Composable
fun Activites(navController: NavController, activitiesViewModel : ActivitesViewModel) {

    val test = activitiesViewModel.activitesData.observeAsState()

    LazyColumn(
        reverseLayout = true
    ) {
        items(test.value?.size ?: 0) { index ->
            Text(text = test.value?.get(index) ?: "No Data")
        }
    }
}