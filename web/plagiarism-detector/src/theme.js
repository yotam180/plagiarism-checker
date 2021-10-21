import { createTheme } from "@material-ui/core";

export default createTheme({
  palette: {
    primary: {
      main: "#4cc08c",
    },
  },
  typography: {
    h1: {
      fontSize: "2rem",
      color: "white",
      fontWeight: 700,
    },
  },
  overrides: {
    MuiTooltip: {
      tooltip: {
        minHeight: "50px",
        backgroundColor: "transparent",
        color: "red",
      },
    },
  },
});
