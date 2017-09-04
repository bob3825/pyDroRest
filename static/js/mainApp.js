var app = angular.module("mainApp", ['ngWebSocket']);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common["X-Requested-With"] = 'XMLHttpRequest';
}]);

app.controller("mainController", function($scope, $http) {
    $scope.products = "Test";

    $scope.leftFront = function() {
        alert('leftFront');
    };

    $scope.front = function() {
        $http.get('droPyRest/v0.1/front').then(
            function successCallback(response) {
                $scope.value1 = response.data['direction'];
                alert($scope.value1);
            },
            function errorCallback(response) {
                $scope.error = 'ERROR';
            }
        );
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