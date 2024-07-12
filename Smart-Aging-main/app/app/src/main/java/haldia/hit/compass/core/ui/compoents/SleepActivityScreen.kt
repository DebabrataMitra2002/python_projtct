package haldia.hit.compass.core.ui.compoents

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.widthIn
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
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
import com.patrykandpatrick.vico.core.extension.mutableListOf
import java.time.LocalDate
import java.time.format.DateTimeFormatter
import kotlin.time.DurationUnit
import kotlin.time.toDuration

@Composable
fun SleepActivity(
    modifier: Modifier = Modifier
) {

    val refreshDataset = remember {
        mutableIntStateOf(0)
    }

    val modelProducer = remember {
        ChartEntryModelProducer()
    }

    val datasetForModel = remember {
        mutableListOf(listOf<FloatEntry>())
    }

    val dataset = remember {
        mutableListOf<Pair<String, Int>>(
            listOf(
                "2015-03-05" to 3660,
                "2015-03-06" to 28020,
                "2015-03-07" to 30360,
                "2015-03-08" to 33300,
                "2015-03-09" to 31020,
                "2015-03-10" to 27960,
                "2015-03-11" to 27840,
            )
        )
    }

    val avg = remember {
        mutableStateOf("")
    }


    LaunchedEffect(key1 = refreshDataset.intValue) {
        datasetForModel.clear()

        var sum = 0
        dataset.forEach {
            val xValue = LocalDate.parse(it.first).toEpochDay().toFloat()
            val yValue = it.second.toFloat()

            sum += it.second
            datasetForModel.add(
                (FloatEntry(xValue, yValue))
            )
        }


        avg.value = (sum / dataset.size
                ).toDuration(DurationUnit.SECONDS).toString()

        modelProducer.setEntries(datasetForModel)

    }


    val verticalAxisValueFormatter =
        AxisValueFormatter<AxisPosition.Vertical.Start> { value, _ ->
            value.toInt().toDuration(DurationUnit.SECONDS)
                .toString(DurationUnit.HOURS)
        }

    val dateTimeFormatter: DateTimeFormatter = DateTimeFormatter.ofPattern("EE")

    val horizontalAxisValueFormatter =
        AxisValueFormatter<AxisPosition.Horizontal.Bottom> { value, _ ->
            (LocalDate.ofEpochDay(value.toLong())).format(dateTimeFormatter)
        }



    Column(
        modifier = modifier,
        verticalArrangement = Arrangement.spacedBy(10.dp)
        ) {
        Text(
            text ="Sleep Activity",
            style = MaterialTheme.typography.titleLarge
        )
        Row(
            horizontalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            AverageSleepDurationCard(
                type = "Average",
                amount = avg.value
            )
            AverageSleepDurationCard(
                type = "Today",
                amount = dataset.last()
                                .second
                                .toDuration(DurationUnit.SECONDS)
                                .toString()
            )
        }
        Chart(
            modifier = Modifier.height(200.dp)
                .padding(10.dp)           ,
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
                valueFormatter = verticalAxisValueFormatter,
            ),
            bottomAxis = rememberBottomAxis(
                valueFormatter = horizontalAxisValueFormatter,
                title = "Weekday",
                titleComponent = textComponent {
                    this.color = MaterialTheme.colorScheme.primary.toArgb()
                },
                guideline = null
            ),
        )
        /*FilledTonalButton(onClick = {
            dataset.clear()
            when (refreshDataset.intValue % 2) {
                0 -> dataset.addAll(
                    listOf(
                        "2015-03-21" to 36600,
                        "2015-03-22" to 36000,
                        "2015-03-23" to 36360,
                        "2015-03-24" to 31800,
                        "2015-03-25" to 35460,
                        "2015-03-26" to 24780,
                        "2015-03-27" to 14340,
                    )
                )

                1 -> dataset.addAll(
                    listOf(
                        "2015-03-27" to 15420,
                        "2015-03-28" to 28860,
                        "2015-03-29" to 24240,
                        "2015-03-30" to 28680,
                        "2015-03-31" to 29880,
                        "2015-04-01" to 28260,
                        "2015-04-02" to 30480,
                    )
                )

                2 -> dataset.addAll(
                    listOf(
                        "2015-04-03" to 27180,
                        "2015-04-04" to 31380,
                        "2015-04-05" to 31800,
                        "2015-04-06" to 27180,
                        "2015-04-07" to 30780,
                        "2015-04-08" to 26340,
                        "2015-04-09" to 26160,
                    )
                )
            }

            refreshDataset.intValue += 1
        }) {
            Text(text = "Reset")
        }*/
    }
}



@Composable
fun AverageSleepDurationCard(
    type: String,
    amount: String
) {
    Card(
        modifier = Modifier.widthIn(min = 100.dp)
    ) {
        Column(
            modifier = Modifier.padding(8.dp)
        ) {

            Text(
                text = type,
                style = MaterialTheme.typography.labelSmall
            )
            Text(
                text = amount,
                style = MaterialTheme.typography.bodyLarge.copy(
                    color = MaterialTheme.colorScheme.primary
                )

            )
        }
    }
}

@Preview
@Composable
fun AverageSleepDurationCardPreview() {
    AverageSleepDurationCard(type = "Average" , amount = "12h 13m 42s")
}