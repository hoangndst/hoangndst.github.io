import { Grid } from '@material-ui/core'
import React from 'react'
import LineChart from '../Charts/LineChart'

export default function Summary({ report }) {
    return (
        <div style={{ height: '500px', marginTop: 10 }}>
          <Grid container spacing={3}>
            <Grid item sm={8} xs={12}>
              <LineChart data={report} />
            </Grid>
            <Grid item sm={4} xs={12}>
            </Grid>
          </Grid>
        </div>
      );
}
