import Typography from "@material-ui/core/Typography";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";

const Header = () => {
  return (
    <AppBar>
      <Toolbar>
        <Typography variant="h1">Plagiarism Detector</Typography>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
