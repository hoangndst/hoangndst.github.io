import React, { useEffect, useState } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';
import moment from 'moment';
import { Button, ButtonGroup } from '@material-ui/core';

const generateOptions = (data) => {
    const categories = data.map((item) => moment(item.Date).format('DD/MM/YYYY'));
    return {
        chart: {
            height: 500,
            type: 'spline'
        },
        title: {
            text: 'Coronavirus Cases'
        },
        xAxis: {
            categories: categories
        },
        colors: ['#1976d2'],
        yAxis: {
            min: 0,
            title: {
              text: null,
            },
            labels: {
              align: 'right',
            },
        },
        tooltip: {
            // headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            // pointFormat:
            //     '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            //     '<td style="padding:0"><b>{point.y} cases</b></td></tr>',
            // footerFormat: '</table>',
            // shared: true,
            // useHTML: true,
            crosshairs: true,
            shared: true
        },
        plotOptions: {
            spline: {
                marker: {
                    radius: 4,
                    lineColor: '#1976d2',
                    lineWidth: 1
                }
            }
        },
        series: [{
            name: 'Coronavirus Cases',
            marker: {
                symbol: 'circle'
            },
            data: data.map((item) => item.Confirmed)
    
        }]
    };
};


export default function LineChart({ data }) {
    console.log('Line Chart', data)
    const [option, setOption] = useState({});
    const [reportType, setReportType] = useState('all');
    
    useEffect(() => {
        let customData = [];
        if (reportType === 'all') {
            customData = data;
        } else if (reportType === '7') {
            customData = data.slice(data.length - 7);
        } else if (reportType === '30') {
            customData = data.slice(data.length - 30);
        } else if (reportType === '1') {
            customData = data.slice(data.length - 365);
        } else {
            customData = data;
        }

        setOption(generateOptions(customData));
    }, [data, reportType])

    return (
        <div>
           <HighchartsReact 
            highcharts={Highcharts}
            options={ option }
           /> 
            <ButtonGroup size='small' style={{ display: 'flex', justifyContent: 'center'}}>
                <Button color={reportType === 'all' ? 'primary' : ''} onClick={() => setReportType('all')}>ALL</Button>
                <Button color={reportType === '7' ? 'primary' : ' '} onClick={() => setReportType('7')}>7 Days</Button>
                <Button color={reportType === '30' ? 'primary' : ' '} onClick={() => setReportType('30')}>30 Days</Button>
                <Button color={reportType === '1' ? 'primary' : ' '} onClick={() => setReportType('1')}>1 Year</Button>
            </ButtonGroup>
        </div>
    )
}
