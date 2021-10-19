import {
  Button,
  Card,
  CardHeader,
  makeStyles,
  TextField,
  Tooltip,
} from "@material-ui/core";
import React from "react";

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
  highlighted: {
    borderRadius: 10,
    paddingLeft: "0.4rem",
    paddingRight: "0.4rem",
    marginRight: "0.2rem",
    cursor: "pointer",
    transition: "background-image 0.2s ease-in-out",

    "&:hover": {
      textDecoration: "underline",
      textDecorationThickness: 2,
      backgroundImage: "linear-gradient(rgba(0, 0, 0, 0.2) 0 0)",
    },
  },
  suspectCard: {
    padding: "1rem",
    fontSize: "0.95rem",
    minWidth: "30rem",
  },
}));

const count_newlines = (text) => {
  for (let i in text) {
    if (text[i] != "\n") {
      return i;
    }
  }

  return text.length;
};

const HighlightedSentence = ({ text, color, suspect }) => {
  const classes = useStyles();

  const colors = {
    red: "#fb8fa3",
    orange: "#fed087",
    yellow: "#fefccf",
  };
  const hardColors = {
    red: "#ea526f",
    orange: "#e89005",
    yellow: "transparent",
  };

  const make_span = () => (
    <span
      style={{
        backgroundColor: colors[color],
        textDecorationColor: hardColors[color] || "transparent",
      }}
      className={color ? classes.highlighted : undefined}
    >
      {text}
    </span>
  );

  const make_newlines = (n) => {
    let els = [];
    for (let i = 0; i < n; ++i) {
      els.push(<br key={"br" + i} />);
    }
    return els;
  };

  console.log(text, count_newlines(text));

  return (
    <>
      {make_newlines(count_newlines(text))}
      {color ? (
        <Tooltip
          interactive
          title={
            <Card className={classes.suspectCard}>
              Sentence found in{" "}
              <a href={suspect.document} target="_blank">
                {suspect.document}
              </a>{" "}
              with {Math.round(suspect.score * 1000) / 10}% confidence
              <br />
              <div
                style={{
                  fontStyle: "italic",
                  color: "#333",
                  backgroundColor: "whitesmoke",
                  padding: "0.5rem",
                  borderRadius: 5,
                  marginTop: "0.6rem",
                }}
              >
                "{suspect.sentence}"
              </div>
            </Card>
          }
        >
          {make_span()}
        </Tooltip>
      ) : (
        make_span()
      )}
      &nbsp;
    </>
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
