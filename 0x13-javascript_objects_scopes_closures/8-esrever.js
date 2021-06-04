#!/usr/bin/node
exports.esrever = function (list) {
  let temp;
  let j = list.length - 1;
  for (let i = 0; i < j; i++, j--) {
    temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return list;
};
