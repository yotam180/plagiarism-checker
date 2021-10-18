import {
  Card,
  CardContent,
  CardHeader,
  CircularProgress,
  makeStyles,
  Modal,
  Typography,
  useMediaQuery,
  useTheme,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  modalCard: {
    position: "absolute",
    top: "50%",
    left: "50%",
    outline: "none",
    border: "none",
    transform: "translate(-50%, -50%)",
    backgroundColor: "white",
    textAlign: "center",

    width: "25rem",
    height: "14rem",
    [theme.breakpoints.down("sm")]: {
      width: "15rem",
      height: "10rem",
    },
  },
  processingText: {
    marginBottom: "2rem",
    [theme.breakpoints.down("sm")]: {
      marginBottom: "0.5rem",
    },
  },
  processingDescription: {
    marginTop: "1.5rem",
    [theme.breakpoints.down("sm")]: {
      marginTop: "0.5rem",
    },
  },
}));

const ProcessModal = ({ open }) => {
  const classes = useStyles();
  const theme = useTheme();
  const matchesSM = useMediaQuery(theme.breakpoints.down("sm"));

  return (
    <Modal open={open}>
      <Card className={classes.modalCard}>
        <CardContent>
          <Typography
            variant={matchesSM ? "h6" : "h4"}
            className={classes.processingText}
          >
            Processing Text
          </Typography>
          <CircularProgress />
          <Typography
            variant="subtitle2"
            className={classes.processingDescription}
          >
            Searching Google (10%)
          </Typography>
        </CardContent>
      </Card>
    </Modal>
  );
};

export default ProcessModal;
