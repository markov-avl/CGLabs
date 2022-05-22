var bspline = require('b-spline');

var points = [
  [-1.0,  0.0],
  [-0.5,  0.5],
  [ 0.5, -0.5],
  [ 1.0,  0.0]
];

var degree = 2;

// As we don't provide a knot vector, one will be generated 
// internally and have the following form :
//
// var knots = [0, 1, 2, 3, 4, 5, 6];
//
// Knot vectors must have `number of points + degree + 1` knots.
// Here we have 4 points and the degree is 2, so the knot vector 
// length will be 7.
//
// This knot vector is called "uniform" as the knots are all spaced uniformly,
// ie. the knot spans are all equal (here 1).

for(var t=0; t<1; t+=0.01) {
  var point = bspline(t, degree, points);
  console.log(point)
}