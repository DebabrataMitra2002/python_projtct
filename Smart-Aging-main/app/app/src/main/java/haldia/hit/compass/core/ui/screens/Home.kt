package haldia.hit.compass.core.ui.screens

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import haldia.hit.compass.core.main.MainViewModel
import haldia.hit.compass.core.ui.compoents.PlugsTrackingActivity
import haldia.hit.compass.core.ui.compoents.SleepActivity


@Composable
fun Home(navController: NavController, model: MainViewModel) {
    Column(
        modifier = Modifier.padding(
            horizontal = 16.dp,
        )
    ) {
        SleepActivity()
        PlugsTrackingActivity(model = model)
    }
}