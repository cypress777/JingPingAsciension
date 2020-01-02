var helloApp = angular.module('helloApp', ['ngAnimate']);

helloApp.controller('helloController', function() {
    this.hideIntro=true;
    this.hideRules=true;
    this.hideTips=true;
});
