import React from 'react'
import { Card, CardContent, Typography, makeStyles } from '@material-ui/core'

const useStyles = makeStyles({
    wrapper: (props) => {
        if (props.type === 'confirmed') return { borderLeft: '5px solid black' };
        if (props.type === 'recovered') return { borderLeft: '5px solid green' };
        else return { borderLeft: '5px solid red' };
    },
    title: {
        fontSize: 18,
        
        color: 'black'
    },
    count: {
        fontSize: 18,
        fontWeight: 'bold',
        color: 'black'
    }
})

export default function HighlightCard({ title, count, type }) {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const styles = useStyles({ type });
    return (
        <Card className={styles.wrapper}>
            <CardContent>
                <Typography component="p" variant="body2" className={styles.title}>
                    {title}
                </Typography>
                <Typography component="span" variant="body2" className={styles.count}>
                    {count}
                </Typography>
            </CardContent>
        </Card>
    )
}
