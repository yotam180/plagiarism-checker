import ThemeProvider from "@material-ui/styles/ThemeProvider";
import Header from "./Header";

import theme from "./theme";

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <Header />
      </ThemeProvider>
    </div>
  );
}

export default App;
