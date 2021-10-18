import Typography from "@material-ui/core/Typography";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import { makeStyles, mergeClasses } from "@material-ui/styles";

const HEADER_HEIGHT = "4rem";

const useStyles = makeStyles((theme) => ({
  header: {
    height: HEADER_HEIGHT,
  },
  headerMargin: {
    height: HEADER_HEIGHT,
  },
}));

const Header = () => {
  const classes = useStyles();

  return (
    <>
      <AppBar elevation={0} className={classes.header}>
        <Toolbar>
          <Typography variant="h1">Plagiarism Detector</Typography>
        </Toolbar>
      </AppBar>

      <div className={classes.headerMargin}>&nbsp;</div>
    </>
  );
};

export default Header;
