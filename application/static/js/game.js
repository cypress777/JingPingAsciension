var app = angular.module('gameApp', []);

app.controller('gameCtrl', gameSetting);

app.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{a');
    $interpolateProvider.endSymbol('a}');
}]);

function getRandInt(min, max) {
    len = max - min;
    return min + Math.floor(len * Math.random());
}

class Card {
    constructor(name, cost, effect, id, description)
}

class HeroCard extends Card {
    constructor(name, cost, effect, faction, honor, rarity, avail, id, description) {
        this.id = id;
        this.name = name;
        this.cost = cost;
        this.effect = effect;
        this.faction = faction;
        this.honor = honor;
        this.rarity = rarity;
        this.avail = avail;
        this.description = description;
    }
}

class ConstructCard extends Card {
    constructor(name, cost, effect, faction, honor, rarity, avail, id, description) {
        this.id = id;
        this.name = name;
        this.cost = cost;
        this.effect = effect;
        this.faction = faction;
        this.honor = honor;
        this.rarity = rarity;
        this.avail = avail;
        this.description = description;
    }
}

class MonsterCard extends Card {
    constructor(name, cost, effect, reward, rarity, avail, id, description) {
        this.id = id;
        this.name = name;
        this.cost = cost;
        this.effect = effect;
        this.reward = reward;
        this.rarity = rarity;
        this.avail = avail;
        this.description = description;
    }
}

class UserState {
    constructor() {
        this.readyDrawCard = false;
        this.honorPoints = 0;
        this.onHand = null;
        this.openHand = null;
        this.startingHand = null;
        this.personalDeck = null;
        this.discardPile = null;
        IntersectionObserver(0)
    }
}

function gameSetting($scope, $document) {
    $scope.user = null;
    $scope.counter = null;
    $scope.centerRow = null;
    $scope.centerDeck = null;
    $scope.voidDeck = null;

    $scope.shuffleCards = function(cards, num) {
        new_cards = [];
        drawed = [];

        i = 0;
        id = getRandInt(0, cards.length);
        while (i < num) {
            while (id in drawed) {
                id = getRandInt(0, cards.length)
            }

            new_cards.push(cards[id]);
            drawed.push(id);

            i += 1;
        }

        return new_cards;
    }

    $scope.drawCard = function(card) {
        if ($scope.user != null && $scope.user.readyDrawCard) {
            card.avail = false;
            $scope.user.readyDrawCard = false;
        }
    };

    $document.ready(function() {
        $scope.user = new UserState();
        $scope.counter = new UserState();

    });
};
