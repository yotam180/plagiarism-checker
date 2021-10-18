import { Button, Card, makeStyles, TextField } from "@material-ui/core";

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
}));

const count_newlines = (text) => {
  for (let i in text) {
    if (text[i] != "\n") {
      return i;
    }
  }

  return text.length;
};

const HighlightedSentence = ({ text, color }) => {
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

  return (
    <>
      {[...new Array(count_newlines(text))].map(() => (
        <br />
      ))}
      <span
        style={{
          backgroundColor: colors[color],
          textDecorationColor: hardColors[color] || "transparent",
        }}
        className={color ? classes.highlighted : undefined}
      >
        {text}
      </span>
      &nbsp;
    </>
  );
};

const show_analysis = (analysis) => {
  let els = [];
  for (var sentence of analysis) {
    if (!sentence.suspect) {
      els.push(<HighlightedSentence text={sentence.sentence} />);
    } else {
      els.push(
        <HighlightedSentence
          text={sentence.sentence}
          color={
            sentence.suspect.score >= 1.0
              ? "red"
              : sentence.suspect.score >= 0.97
              ? "orange"
              : "yellow"
          }
        />
      );
    }
  }

  return els;
};

const TextArea = ({ editable, rawText, analysis, onChange, onSubmit }) => {
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
                onClick={onSubmit}
              >
                Check for Plagiarism
              </Button>
            </div>
          </Card>
        </div>
      </div>
    </>
  );
};

export default TextArea;
