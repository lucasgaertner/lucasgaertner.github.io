var width = 960,
height = 630;
 
 
d3.select("#bubbleChart").append("svg")
    .attr("width", width)
    .attr("height", height)
	.attr("id", "primarySVG");
 
 
changeYear('2015');
 
$("label.cycleBtn").click(function() {
	changeYear(this.id);
	
	});
 
	
function changeYear(year){
	var CSV2015 = 'bubbleChart2015.csv';
	var CSV2014 = 'bubbleChart2014.csv';
	if (year === '2015'){
		var dataSource = CSV2015;
	} else {
		var dataSource = CSV2014;
	}
 
 
d3.csv(dataSource, function(error, data) {
 
data.sort(function(a,b) {return b.ratingClassValue - a.ratingClassValue;});
 
 
var svg = d3.select("#primarySVG");
	
 
 
//set bubble padding
var padding = 4;
 
  for (var j = 0; j < data.length; j++) {
    data[j].radius = 10;
    data[j].x = Math.random() * width;
    data[j].y = Math.random() * height;
  }
 
  var maxRadius = d3.max(_.pluck(data, 'radius'));
 
 
  var getCenters = function(vname, size) {
    var centers, map;
    centers = _.uniq(_.pluck(data,vname)).map(function(d) {
      return {
        name: d,
        value: 1
      };
    });
 
	map = d3.layout.pack().size(size);
          map.nodes({children: centers});
 
    return centers;
  };
 
	var nodes = svg.selectAll("circle")
		.data(data);
	
  nodes.enter().append("circle")
    //.attr("class", "node")
     .attr("class", function(d) {
      return d.ratingCategory;
    })
    .attr("cx", function(d) {
      return d.x;
    })
    .attr("cy", function(d) {
      return d.y;
    })
    .attr("r", 2)
	.attr("id", function(d){return d.objectName;})
    .on("mouseover", function(d) {
      showPopover.call(this, d);
    })
    .on("mouseout", function(d) {
      removePopovers();
    })
	;
 
	var text = nodes.append("text")
		.attr("dx",12)
		.attr("dy",".35em")
		.text(function(d){
			return d.objectName;
		});
 
		
	
  nodes.transition()
	.duration(500)
    .attr("r", function(d) {
	return d.radius;})
	;
 
  var force = d3.layout.force();
  
 
  draw('reset');
 
 $("label.ratingBtn").click(function() {
   	draw(this.id);
	});
  
  
 
 function draw(varname) {
 	d3.selectAll("circle").attr("r",10);
	var centers = getCenters(varname, [width, height]);
    force.on("tick", tick(centers, varname));
    labels(centers);
	nodes.attr("class", function(d) {
      return d[varname];
    });
    force.start();
	makeClickable();
  }
 
	
	function tick (centers, varname) {
	  var foci = {};
	  for (var i = 0; i < centers.length; i++) {
		foci[centers[i].name] = centers[i];
	  }
	  return function (e) {
		for (var i = 0; i < data.length; i++) {
		  var o = data[i];
		  var f = foci[o[varname]];
		  o.y += (f.y - o.y) * e.alpha;
		  o.x += (f.x - o.x) * e.alpha;
		 }
		 nodes.each(collide(.2))
		   .attr("cx", function (d) { return d.x; })
		   .attr("cy", function (d) { return d.y; });
	  }
	}
	
		
  function labels(centers) {
    svg.selectAll(".label").remove();
 
    svg.selectAll(".label")
      .data(centers).enter().append("text")
      .attr("class", "label")
      .text(function(d) {
        return d.name;
      })
	.attr("transform", function (d) {
            return "translate(" + (d.x - ((d.name.length)*3)) + ", " + (d.y + 15 - d.r) + ")";
          });     
 
 
  }
 
  function removePopovers() {
    $('.popover').each(function() {
      $(this).remove();
    });
  }
 
  function showPopover(d) {
    $(this).popover({
      placement: 'auto top',
      container: 'body',
      trigger: 'manual',
      html: true,
      content: function() {
        return "Assessment ID: " + d.objectName + "</br>Risk Category 1: " + d.riskCategory1 + "</br>Risk Category 2: " + d.riskCategory2;
      }
    });
    $(this).popover('show');
  }
  
  function collide(alpha) {
    var quadtree = d3.geom.quadtree(data);
    return function(d) {
       var r = d.radius + maxRadius + padding,
        nx1 = d.x - r,
        nx2 = d.x + r,
        ny1 = d.y - r,
        ny2 = d.y + r;
      quadtree.visit(function(quad, x1, y1, x2, y2) {
        if (quad.point && (quad.point !== d)) {
          var x = d.x - quad.point.x,
            y = d.y - quad.point.y,
            l = Math.sqrt(x * x + y * y),
            r = d.radius + quad.point.radius + padding;
          if (l < r) {
            l = (l - r) / l * alpha;
            d.x -= x *= l;
            d.y -= y *= l;
            quad.point.x += x;
            quad.point.y += y;
          }
        }
        return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
      });
    };
  }
  
   var lowModGrad = svg.append("svg:defs")
    .append("svg:linearGradient")
    .attr("id", "lowModGrad")
    .attr("x1", "0%")
    .attr("y1", "0%")
    .attr("x2", "100%")
    .attr("y2", "100%")
    .attr("spreadMethod", "pad");
 
  // Define the gradient colors
  lowModGrad.append("svg:stop")
    .attr("offset", "0%")
    .attr("stop-color", "#88DB54")
    .attr("stop-opacity", 1);
 
  lowModGrad.append("svg:stop")
    .attr("offset", "100%")
    .attr("stop-color", "#FE9A2E")
    .attr("stop-opacity", 1);
 
  var modHighGrad = svg.append("svg:defs")
    .append("svg:linearGradient")
    .attr("id", "modHighGrad")
    .attr("x1", "0%")
    .attr("y1", "0%")
    .attr("x2", "100%")
    .attr("y2", "100%")
    .attr("spreadMethod", "pad");
 
  // Define the gradient colors
  modHighGrad.append("svg:stop")
    .attr("offset", "0%")
    .attr("stop-color", "#FE9A2E")
    .attr("stop-opacity", 1);
 
  modHighGrad.append("svg:stop")
    .attr("offset", "100%")
    .attr("stop-color", "#FE2E2E")
    .attr("stop-opacity", 1);
    
  var lowHighGrad = svg.append("svg:defs")
    .append("svg:linearGradient")
    .attr("id", "lowHighGrad")
    .attr("x1", "0%")
    .attr("y1", "0%")
    .attr("x2", "100%")
    .attr("y2", "100%")
    .attr("spreadMethod", "pad");
 
  // Define the gradient colors
  lowHighGrad.append("svg:stop")
    .attr("offset", "0%")
    .attr("stop-color", "#88DB54")
    .attr("stop-opacity", 1);
 
  lowHighGrad.append("svg:stop")
    .attr("offset", "100%")
    .attr("stop-color", "#FE2E2E")
    .attr("stop-opacity", 1);
 
	
 
	function makeClickable () {
		
				
	$("circle").click(function() {
   	console.log(this.id);
	});
	
	var nest = d3.nest()
		.key(function(d){return d.objectName;})
		.entries(data);
		
	
	}
	nodes.exit().remove();
		
	
});
}