package haldia.hit.compass.core.ui.compoents

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.unit.dp
import haldia.hit.compass.core.main.MainViewModel
import com.patrykandpatrick.vico.compose.axis.horizontal.rememberBottomAxis
import com.patrykandpatrick.vico.compose.axis.vertical.rememberStartAxis
import com.patrykandpatrick.vico.compose.chart.Chart
import com.patrykandpatrick.vico.compose.chart.column.columnChart
import com.patrykandpatrick.vico.core.axis.AxisPosition
import com.patrykandpatrick.vico.core.axis.formatter.AxisValueFormatter
import com.patrykandpatrick.vico.core.component.shape.LineComponent
import com.patrykandpatrick.vico.core.component.shape.Shapes
import com.patrykandpatrick.vico.core.component.text.textComponent
import com.patrykandpatrick.vico.core.entry.ChartEntryModelProducer
import com.patrykandpatrick.vico.core.entry.FloatEntry
import kotlin.time.DurationUnit
import kotlin.time.toDuration

@Composable
fun PlugsTrackingActivity(
    model: MainViewModel,
    modifier: Modifier = Modifier
) {

    val test = model.plugsAverageData.collectAsState()
    val xlables = remember {
        mutableListOf<String>()
    }
    val modelProducer = remember {
        ChartEntryModelProducer()
    }

    val datasetForModel = remember {
        mutableListOf<FloatEntry>()
    }

    // Whenever data changes, this effects is called.
    LaunchedEffect(key1 = test.value) {
        datasetForModel.clear()
        when (test.value) {
            is MainViewModel.PlugsAverageEvent.Success -> {
                val data = (test.value as MainViewModel.PlugsAverageEvent.Success).successData
                var xp = 0
                data.forEach {
                    datasetForModel.add(
                        FloatEntry(xp.toFloat(), it.averge_duration.toFloat())
                    )
                    xlables.add(it.type)
                    xp += 1
                }
                modelProducer.setEntries(datasetForModel)
            }
            else -> Unit
        }
    }

    val horizontalAxisValueFormatter =
        AxisValueFormatter<AxisPosition.Horizontal.Bottom> { value, _ ->
            xlables.getOrNull(value.toInt()) ?: ""
        }

    val verticalAxisValueFormatter =
        AxisValueFormatter<AxisPosition.Vertical.Start> { value, _ ->
            value.toInt().toDuration(DurationUnit.SECONDS).toString()
        }


    // Fetches data only once, when screen is first launched
    LaunchedEffect(Unit) {
        model.getPlugsAverageData()
    }


    Column(modifier = modifier,
        verticalArrangement = Arrangement.spacedBy(10.dp)
        ) {
        Text(
            text ="User's Activity",
            style = MaterialTheme.typography.titleLarge
        )
        when (test.value) {
            is MainViewModel.PlugsAverageEvent.Loading -> {
                LinearProgressIndicator(
                    modifier.fillMaxWidth()
                )
            }
            is MainViewModel.PlugsAverageEvent.Empty -> {
                Text(text = "Empty")
            }

            is MainViewModel.PlugsAverageEvent.Failure -> {
                Text(text = "Failed to load.")
            }

            is MainViewModel.PlugsAverageEvent.Success -> {
                Chart(
                    modifier = Modifier.height(150.dp),
                    chart = columnChart(
                        columns = listOf(
                            LineComponent(
                                color = MaterialTheme.colorScheme.primary.toArgb(),
                                thicknessDp = 5f,
                                shape = Shapes.roundedCornerShape(
                                    topLeftPercent = 20,
                                    topRightPercent = 20
                                )
                            ),
                        ),
                        spacing = 10.dp,
                    ),
                    chartModelProducer = modelProducer,
                    startAxis = rememberStartAxis(
                       valueFormatter = verticalAxisValueFormatter
                    ),
                    bottomAxis = rememberBottomAxis(
                       valueFormatter = horizontalAxisValueFormatter,
                        title = "Activities",
                        titleComponent = textComponent {
                            this.color = MaterialTheme.colorScheme.primary.toArgb()
                        },
                        guideline = null
                    ),
                )
            }
        }
    }

}
