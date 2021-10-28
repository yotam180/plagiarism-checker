import ThemeProvider from "@material-ui/styles/ThemeProvider";
import Header from "./Header";
import ProcessModal from "./ProcessModal";
import TextArea from "./TextArea";

import "./global.css";

import theme from "./theme";
import SSE from "./sse";
import { useState } from "react";

const States = {
  EDITING: "EDITING",
  PROCESSING: "PROCESSING",
  DONE: "DONE",
};

const REMOTE_URL =
  process.env.REACT_APP_REMOTE_URL || "http://localhost:8080/process";

function App() {
  const [state, setState] = useState(States.EDITING);
  const [text, setText] = useState("");
  const [loadingText, setLoadingText] = useState("");
  const [analysis, setAnalysis] = useState([
    {
      sentence: "Hello, world!",
      suspect: {
        document: "https://google.com/q?",
        sentence: "Hello, world!!!",
        score: 0.96,
      },
    },
  ]);

  const onSubmit = () => {
    requestProcessing(text);
    setLoadingText("Uploading text...");
    setState(States.PROCESSING);
  };

  const requestProcessing = (text) => {
    let sse = SSE(REMOTE_URL, { payload: text });
    sse.onerror = (e) => {
      console.error(e);
      alert("An error occurred!"); // TODO: Prettier error message...
    };
    sse.onmessage = (e) => {
      let data = JSON.parse(e.data);
      if (data.type === "LOADING") {
        setLoadingText(data.text);
      } else if (data.type === "DONE") {
        let results = data.text;
        console.log(results);
        setState(States.DONE);
        setAnalysis(results);
      } else if (data.type === "ERROR") {
        alert(data.text);
      }
    };
  };

  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <Header />
        <TextArea
          editable={state === States.EDITING || state === States.PROCESSING}
          rawText={text}
          analysis={analysis}
          onChange={(e) => setText(e.target.value)}
          onSubmit={onSubmit}
          onReturn={() => setState(States.EDITING)}
        />
        {state == States.PROCESSING && <ProcessModal open text={loadingText} />}
      </ThemeProvider>
    </div>
  );
}

export default App;
