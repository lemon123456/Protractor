'use strict';

describe('Angular Demo', function() {
    it('should have a title', function() {
        browser.get('/');
        expect(element(by.css('.navbar-brand')).getText()).toEqual('OneCloud Test');
    });
});
