import { Button, Card, makeStyles } from "@material-ui/core";
import React from "react";
import Sentence from "./Components/Sentence";
import SuspectCard from "./Components/SuspectCard";

const useStyles = makeStyles((theme) => ({
  textArea: {
    backgroundColor: "whitesmoke",
    position: "fixed",
    display: "flex",
    justifyContent: "center",
    top: "4rem",
    bottom: 0,
    right: 0,
    left: 0,
  },
  cardContainer: {
    display: "flex",
    flex: 1,
    maxWidth: "90rem",
  },
  textareaCard: {
    flex: 1,
    display: "flex",
    margin: "2em",
    marginBottom: "4em",
    borderRadius: 15,
  },
  textBox: {
    flex: 1,
    backgroundColor: "transparent",
    lineHeight: "2rem",

    overflowY: "auto",

    border: "none",
    outline: "none",
    resize: "none",
    margin: "1em",

    fontSize: "1.15rem",
    fontFamily: "Roboto Slab",
  },
  processButtonDiv: {
    position: "absolute",
    bottom: "2.5em",
    textAlign: "center",
    left: 0,
    right: 0,
  },
  processButton: {
    paddingTop: ".8em",
    paddingBottom: ".8em",
    textTransform: "none",
    fontSize: "1rem",
    borderRadius: 50,
    color: "white",
  },
}));

const HighlightedSentence = ({ text, color, suspect }) => {
  return (
    <Sentence
      text={text}
      color={color}
      tooltipComponent={
        <SuspectCard
          articleURL={suspect && suspect.document}
          score={suspect && suspect.score}
          plagiarisedSentence={suspect && suspect.sentence}
          color={color}
        />
      }
    />
  );
};

const show_analysis = (analysis) => {
  let els = [];
  for (var sentence of analysis) {
    if (!sentence.suspect) {
      els.push(
        <HighlightedSentence key={sentence.sentence} text={sentence.sentence} />
      );
    } else {
      els.push(
        <HighlightedSentence
          key={sentence.sentence}
          text={sentence.sentence}
          suspect={sentence.suspect}
          color={
            sentence.suspect.score >= 0.999
              ? "red"
              : sentence.suspect.score >= 0.975
              ? "orange"
              : "yellow"
          }
        />
      );
    }
  }

  return els;
};

const TextArea = ({
  editable,
  rawText,
  analysis,
  onChange,
  onSubmit,
  onReturn,
}) => {
  const classes = useStyles();

  return (
    <>
      <div className={classes.textArea}>
        <div className={classes.cardContainer}>
          <Card className={classes.textareaCard} elevation={8}>
            {editable ? (
              <textarea
                className={classes.textBox}
                placeholder="Paste your text here..."
                onChange={onChange}
                value={rawText}
              ></textarea>
            ) : (
              <div className={classes.textBox}>{show_analysis(analysis)}</div>
            )}

            <div className={classes.processButtonDiv}>
              <Button
                variant="contained"
                color="primary"
                className={classes.processButton}
                onClick={editable ? onSubmit : onReturn}
              >
                {editable ? "Check for Plagiarism" : "Try again"}
              </Button>
            </div>
          </Card>
        </div>
      </div>
    </>
  );
};

export default TextArea;
