#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const coincidences = list.filter(elem => elem === searchElement);
  return coincidences.length;
};
