var connect = require('connect');
var http = require('http');
var url = require('url');
var jade = require('jade');
var nunjucks = require('nunjucks');
var dust = require('dustjs-linkedin');
var dusthelpers = require('dustjs-helpers');
var randomstring = require("randomstring");
var doT=require('dot');
var marko=require('marko');

var app = connect();

// Jade
app.use('/jade', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    res.end(randomstring.generate() + jade.render(tpl) + randomstring.generate());
  }
});

// Jade blind endpoint
app.use('/blind/jade', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    jade.render(tpl)
    res.end(randomstring.generate());
  }
});

// Nunjucks
app.use('/nunjucks', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    res.end(randomstring.generate() + nunjucks.renderString(tpl) + randomstring.generate());
  }
});

// Nunjucks blind endpoint
app.use('/blind/nunjucks', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    nunjucks.renderString(tpl);
    res.end(randomstring.generate());
  }
});

// Javascript
app.use('/javascript', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    res.end(randomstring.generate() + String(eval(tpl)) + randomstring.generate());
  }
});

// Javascript blind endpoint
app.use('/blind/javascript', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    eval(tpl);
    res.end(randomstring.generate());
  }
});

// Dust
app.use('/dust', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    
    console.log('PAYLOAD: ' + tpl);
    dust.debugLevel = "DEBUG"
    output = '';
    var compiled = dust.compile(tpl, "compiled");
    dust.loadSource(compiled);
    dust.render("compiled", {}, function(err, outp) { output = outp })
    res.end(randomstring.generate() + output + randomstring.generate());
  }
});

// Dust blind endpoint
app.use('/blind/dust', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    
    console.log('PAYLOAD: ' + tpl);
    dust.debugLevel = "DEBUG"
    var compiled = dust.compile(tpl, "compiled");
    dust.loadSource(compiled);
    dust.render("compiled", {}, function(err, outp) { })
    
    res.end(randomstring.generate());
  }
});

// doT
app.use('/dot', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    res.end(randomstring.generate() + doT.template(tpl)({}) + randomstring.generate());
  }
});

// doT blind endpoint
app.use('/blind/dot', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    doT.template(tpl)({});
    res.end(randomstring.generate());
  }
});

// Marko
app.use('/marko', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    res.end(randomstring.generate() + marko.load(randomstring.generate(), tpl).renderSync() + randomstring.generate());
  }
});

// Marko blind endpoint
app.use('/blind/marko', function(req, res){
  if(req.url) {
    var url_parts = url.parse(req.url, true);

    var inj = url_parts.query.inj;
    var tpl = '';
    if('tpl' in url_parts.query) {
      // Keep the formatting a-la-python
      tpl = url_parts.query.tpl.replace('%s', inj);
    }
    else {
      tpl = inj;
    }
    marko.load(randomstring.generate(), tpl).renderSync()
    res.end(randomstring.generate());
  }
});

//create node.js http server and listen on port
http.createServer(app).listen(15004);
