package haldia.hit.compass

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Menu
import androidx.compose.material.icons.filled.MoreVert
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.DpOffset
import androidx.compose.ui.unit.dp
import androidx.navigation.NavDestination.Companion.hierarchy
import androidx.navigation.NavGraph.Companion.findStartDestination
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import dagger.hilt.android.AndroidEntryPoint
import haldia.hit.compass.core.main.ActivitesViewModel
import haldia.hit.compass.core.main.MainViewModel
import haldia.hit.compass.core.ui.screens.Activites
import haldia.hit.compass.core.ui.screens.Home
import haldia.hit.compass.core.ui.screens.Profile
import haldia.hit.compass.core.ui.theme.CompassTheme
import haldia.hit.compass.core.util.MyService

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    @OptIn(ExperimentalMaterial3Api::class)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {

            val items = listOf(
                Screen.Home,
                Screen.Activities,
                Screen.Profile
            )

            CompassTheme {

                val navController = rememberNavController()
                val mainViewModel: MainViewModel by viewModels()
                val activityViewModel: ActivitesViewModel by viewModels()
                var showDropDownMenu by remember { mutableStateOf(false) }


                Scaffold(
                    topBar = {
                        TopAppBar(
                            title = { Text(getString(R.string.app_name)) },
                            actions = {
                                IconButton(onClick = {
                                    showDropDownMenu = true
                                }) {
                                    Icon(
                                        imageVector = Icons.Filled.MoreVert,
                                        contentDescription = "More"
                                    )
                                }

                                DropdownMenu(
                                    expanded = showDropDownMenu,
                                    onDismissRequest = { showDropDownMenu = false },
                                    offset = DpOffset((-40).dp, (-64).dp),
                                ) {
                                    DropdownMenuItem(
                                        text = { Text("Settings") },
                                        onClick = { /* Handle settings! */ }
                                    )
                                    DropdownMenuItem(
                                        text = { Text("About") },
                                        onClick = { /* Handle send feedback! */ }
                                    )

                                }
                            },
                        )
                    },
                    bottomBar = {
                        NavigationBar {
                            val navBackStackEntry by navController.currentBackStackEntryAsState()
                            val currentDestination = navBackStackEntry?.destination
                            items.forEach { screen ->

                                val itemSelected =
                                    currentDestination?.hierarchy?.any { it.route == screen.route } == true
                                val icon = if (itemSelected) screen.selectedIcon else screen.icon

                                NavigationBarItem(
                                    icon = { Icon(icon, contentDescription = null) },
                                    label = { Text(stringResource(screen.resourceId)) },
                                    selected = itemSelected,
                                    onClick = {
                                        navController.navigate(screen.route) {
                                            // Pop up to the start destination of the graph to
                                            // avoid building up a large stack of destinations
                                            // on the back stack as users select items
                                            popUpTo(navController.graph.findStartDestination().id) {
                                                saveState = true
                                            }
                                            // Avoid multiple copies of the same destination when
                                            // reselecting the same item
                                            launchSingleTop = true
                                            // Restore state when reselecting a previously selected item
                                            restoreState = true
                                        }
                                    }
                                )
                            }
                        }
                    }
                ) { innerPadding ->
                    NavHost(
                        navController,
                        startDestination = Screen.Home.route,
                        Modifier.padding(innerPadding)
                    ) {
                        composable(Screen.Home.route) { Home(navController, model = mainViewModel) }
                        composable(Screen.Activities.route) {
                            Activites(
                                navController,
                                activitiesViewModel = activityViewModel
                            )
                        }
                        composable(Screen.Profile.route) { Profile(navController) }
                    }
                }
            }
        }

        try {
            val intent = Intent(this, MyService::class.java) // Build the intent for the service
            applicationContext.startForegroundService(intent)
        } catch (e: Exception) {
            e.printStackTrace()
            Toast.makeText(this, "Service failed to run", Toast.LENGTH_SHORT).show()
        }
    }
}

