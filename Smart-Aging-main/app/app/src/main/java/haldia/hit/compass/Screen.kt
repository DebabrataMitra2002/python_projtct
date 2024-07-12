package haldia.hit.compass

import androidx.annotation.StringRes
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AccountCircle
import androidx.compose.material.icons.filled.BarChart
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.outlined.AccountCircle
import androidx.compose.material.icons.outlined.BarChart
import androidx.compose.material.icons.outlined.Home
import androidx.compose.ui.graphics.vector.ImageVector

sealed class Screen(val route: String, @StringRes val resourceId: Int, val icon: ImageVector, val selectedIcon: ImageVector) {
     object Profile : Screen("profile", R.string.profile, Icons.Outlined.AccountCircle, Icons.Filled.AccountCircle)

     object Activities : Screen("activities", R.string.activities, Icons.Outlined.BarChart, Icons.Filled.BarChart)

     object Home : Screen("home", R.string.home, Icons.Outlined.Home, Icons.Filled.Home)
}