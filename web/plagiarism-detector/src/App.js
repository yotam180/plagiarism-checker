import ThemeProvider from "@material-ui/styles/ThemeProvider";
import Header from "./Header";
import ProcessModal from "./ProcessModal";
import TextArea from "./TextArea";

import "./global.css";

import theme from "./theme";

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <Header />
        <TextArea />
        {/* <ProcessModal open /> */}
      </ThemeProvider>
    </div>
  );
}

export default App;
