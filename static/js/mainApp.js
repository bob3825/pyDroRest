var app = angular.module("mainApp", []);
app.controller("mainController", function($scope) {
    $scope.products = "Test";

    $scope.leftFront = function() {
        alert('leftFront');
    };

    $scope.front = function() {
        alert('front');
    };

    $scope.rightFront = function() {
        alert('rightFront');
    };

    $scope.left = function() {
        alert('left');
    };

    $scope.land = function() {
        alert('land');
    };

    $scope.right = function() {
        alert('right');
    };

    $scope.leftBack = function() {
        alert('leftBack');
    };

    $scope.back = function() {
        alert('back');
    };

    $scope.rightBack = function() {
        alert('rightBack');
    };

    $scope.up = function() {
        alert('up');
    };

    $scope.down = function() {
        alert('down');
    };

    $scope.test = function() {
        alert('test');
    };
});