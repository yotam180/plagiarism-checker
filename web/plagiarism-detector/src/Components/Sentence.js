/**
 * Sentence is a component to show a (potentially) highlighted sentence with a custom tooltip
 */

import { makeStyles, Tooltip } from "@material-ui/core";
import React from "react";

import { countNewlines } from "../textutil";

const useStyles = makeStyles((theme) => ({
  highlightedText: {
    borderRadius: 10,
    paddingLeft: "0.4rem",
    paddingRight: "0.4rem",
    marginRight: "0.2rem",

    cursor: "pointer",

    transition: "background-image 0.2s ease-in-out",

    "&:hover": {
      backgroundImage: "linear-gradient(rgba(0, 0, 0, 0.2) 0 0)",
    },
  },
}));

const makeNewlines = (count) => {
  let elements = [];
  for (let i = 0; i < count; ++i) {
    elements.push(<br key={i} />);
  }
  return elements;
};

const Sentence = ({ text, color, tooltipComponent }) => {
  const classes = useStyles();

  const colors = {
    red: "#fb8fa3",
    orange: "#fed087",
    yellow: "#fefccf",
  };

  const backgroundColor = colors[color] || color;
  const highlighted = Boolean(color || tooltipComponent);

  let textSpan = (
    <span
      style={{ backgroundColor }}
      className={highlighted ? classes.highlightedText : undefined}
    >
      {text}
    </span>
  );

  if (tooltipComponent) {
    textSpan = (
      <Tooltip interactive title={tooltipComponent}>
        {textSpan}
      </Tooltip>
    );
  }

  return (
    <>
      {makeNewlines(countNewlines(text))}
      {textSpan}
      &nbsp;
    </>
  );
};

export default Sentence;
