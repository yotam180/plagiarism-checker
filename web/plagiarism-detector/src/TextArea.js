import { Button, Card, makeStyles, TextField } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  textArea: {
    backgroundColor: "whitesmoke",

    position: "fixed",
    display: "flex",
    top: "4rem",
    bottom: 0,
    right: 0,
    left: 0,
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

const TextArea = () => {
  const classes = useStyles();

  return (
    <>
      <div className={classes.textArea}>
        <Card className={classes.textareaCard} elevation={8}>
          <div
            className={classes.textBox}
            data-placeholder="Paste your text here..."
            contentEditable
          ></div>
          <div className={classes.processButtonDiv}>
            <Button
              variant="contained"
              color="primary"
              className={classes.processButton}
            >
              Check for Plagiarism
            </Button>
          </div>
        </Card>
      </div>
    </>
  );
};

export default TextArea;
