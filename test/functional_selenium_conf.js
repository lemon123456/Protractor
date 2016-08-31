var SpecReporter = require('jasmine-spec-reporter');
var ScreenShotReporter = require('protractor-screenshot-reporter');
var path = require('path');
var fs = require('fs-extra');

// Use seleniumServerJar + phantomjs
exports.config = {

    allScriptsTimeout: 15000,

    // if use seleniumServerJar, do not specify seleniumAddress
    seleniumServerJar: '../node_modules/selenium-standalone/.selenium/2.43.1/server.jar',
    // port of the server
    seleniumPort: 4444,
    seleniumArgs: ['-browserTimeout=60'],

    specs: ['functional/*-spec.js'],

    baseUrl: 'http://localhost:8000',

    framework: 'jasmine2',

    capabilities: {
        browserName: 'phantomjs',
        // This can generally be ommitted if you installed phantomjs globally.
        // 'phantomjs.binary.path': require('phantomjs').path,
        // 'phantomjs.cli.args': ['--ignore-ssl-errors=true', '--web-security=false']
    },

    // phantomjs.binary.path - path to the PhantomJs exec file
    // phantomjs.cli.args - PhantomJs parameters. ['--ignore-ssl-errors=true', '--web-security=false'] force PhantomJs to accept https sites.

    jasmineNodeOpts: {
        defaultTimeoutInterval: 90000,
        print: function () {
        }
    },

    onPrepare: function () {
        fs.removeSync('./functional/screenshots');
        browser.driver.manage().window().setSize(1280, 800);

        jasmine.getEnv().addReporter(new SpecReporter({
            displayFailuresSummary: true,
            displaySpecDuration: true,
            displayStacktrace: 'summary'
        }));

        jasmine.getEnv().addReporter(new ScreenShotReporter({
            baseDirectory: 'functional/screenshots',
            pathBuilder: function pathBuilder(spec, descriptions, results, capabilities) {
                return path.join(descriptions.join('-'));
            },
            takeScreenShotsOnlyForFailedSpecs: true
        }));
    }
}
