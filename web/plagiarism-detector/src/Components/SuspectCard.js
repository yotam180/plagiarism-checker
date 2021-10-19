/**
 * SuspectCard is a tooltip card component that displays where a sentence was
 * taken from.
 */

import {
  Card,
  CircularProgress,
  Grid,
  makeStyles,
  Typography,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  suspectCard: {
    padding: "1rem",
    fontSize: "0.95rem",
    minWidth: "25rem",
  },
  quoteDiv: {
    fontStyle: "italic",
    fontFamily: "Libre Baskerville",
    color: "#333",
    padding: "0.5rem",
    borderRadius: 5,
    marginTop: "0.6rem",
  },
  percentageLabel: {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    fontSize: "1rem",
  },
  percentageContainer: {
    position: "relative",
    textAlign: "center",
  },
  linkContainer: {
    textAlign: "center",
  },
  documentLink: {
    marginTop: "0.5rem",
    fontSize: "1.3rem",
  },
}));

const SuspectCard = ({ articleURL, score, plagiarisedSentence, color }) => {
  const classes = useStyles();

  const confidence = Math.round(score * 1000) / 10;

  const colors = {
    red: "#cc0000",
    orange: "#e68a00",
    yellow: "#b3b300",
  };

  color = colors[color];

  return (
    <Card className={classes.suspectCard}>
      <Grid container direction="column">
        <Grid item container direction="row">
          <Grid item xs={2} className={classes.percentageContainer}>
            <Grid container direction="column" alignItems="center">
              <Grid item className={classes.percentageContainer}>
                <CircularProgress
                  variant="determinate"
                  value={(confidence - 90) * 10}
                  size="3rem"
                  style={{ color }}
                ></CircularProgress>
                <div style={{ color }} className={classes.percentageLabel}>
                  {confidence}
                </div>
              </Grid>
              <Grid item>
                <Typography variant="body2">confidence</Typography>
              </Grid>
            </Grid>
          </Grid>
          <Grid item xs={10} className={classes.linkContainer}>
            <Typography variant="body2">Similar sentence found on:</Typography>
            <div className={classes.documentLink}>
              <a href={articleURL} target="_blank" rel="noreferrer noopener">
                {new URL(articleURL).hostname}
              </a>
            </div>
          </Grid>
        </Grid>
      </Grid>
      <br />
      <div className={classes.quoteDiv}>"{plagiarisedSentence}"</div>
    </Card>
  );
};

export default SuspectCard;
