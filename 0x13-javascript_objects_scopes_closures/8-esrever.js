#!/usr/bin/node
exports.esrever = function (list) {
  const l = list.length / 2;
  for (let i = 0; i < l; i++) {
    const tmp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = tmp;
  }
  return (list);
};
