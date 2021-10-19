/**
 * Counts the number of newlines prefixing a given string
 *
 * @param {String} text The text to be counted
 * @returns The number of newlines at the beginning of the text
 */
export function countNewlines(text) {
  for (let i = 0; i < text.length; ++i) {
    if (text[i] != "\n") {
      return i;
    }
  }

  return text.length;
}
