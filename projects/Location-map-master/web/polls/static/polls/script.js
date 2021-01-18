var current = d3.select("#current")
var canvas = d3.select("#globe")
var context = canvas.node().getContext("2d")
var water = {type: "Sphere"}
var projection = d3.geoOrthographic().precision(0.1)
var graticule = d3.geoGraticule10()
var path = d3.geoPath(projection).context(context)
var currentCountry



// Load Data
function loadData(cb) {
  d3.json('https://unpkg.com/world-atlas@1/world/110m.json', function(error, world) {
    if (error) throw error
    d3.tsv('https://gist.githubusercontent.com/mbostock/4090846/raw/07e73f3c2d21558489604a0bc434b3a5cf41a867/world-country-names.tsv', function(error, countries) {
      if (error) throw error
      cb(world, countries)
    })
  })
}





// scale
function scale() {
  width = document.documentElement.clientWidth
  height = document.documentElement.clientHeight
  canvas.attr('width', width).attr('height', height)
  projection
    .scale((0.9 * Math.min(width, height)) / 2)
    .translate([width / 2, height / 2])
  render()
}

// fill
function fill(obj, color) {
  context.beginPath()
  path(obj)
  context.fillStyle = color


  context.fill()
}

// Mercer
function stroke(obj, color) {
  context.beginPath()
  path(obj)
  context.strokeStyle = "lightblue"
  context.stroke()
}

// render
function render() {
  context.clearRect(0, 0, width, height)
  fill(water, "blue")
  stroke(graticule, "#eee")
  fill(land, "green")
  // Land hover
  if (currentCountry) {
    fill(currentCountry, "lightgreen")
  }
}


// Drag Area
function dragstarted() {
  v0 = versor.cartesian(projection.invert(d3.mouse(this)))
  r0 = projection.rotate()
  q0 = versor(r0)
}

function dragged() {
  var v1 = versor.cartesian(projection.rotate(r0).invert(d3.mouse(this)))
  var q1 = versor.multiply(q0, versor.delta(v0, v1))
  var r1 = versor.rotation(q1)
  projection.rotate(r1)
  render()
}

function dragended() {
  startRotation(rotationDelay)
}

// https://github.com/d3/d3-polygon
function polygonContains(polygon, point) {
  var n = polygon.length
  var p = polygon[n - 1]
  var x = point[0], y = point[1]
  var x0 = p[0], y0 = p[1]
  var x1, y1
  var inside = false
  for (var i = 0; i < n; ++i) {
    p = polygon[i], x1 = p[0], y1 = p[1]
    if (((y1 > y) !== (y0 > y)) && (x < (x0 - x1) * (y - y1) / (y0 - y1) + x1)) inside = !inside
    x0 = x1, y0 = y1
  }
  return inside
}




// Check if we are with mouse in the correct Area
function getCountry(event) {
  var pos = projection.invert(d3.mouse(event))
  return countries.features.find(function(f) {
    return f.geometry.coordinates.find(function(c1) {
      return polygonContains(c1, pos) || c1.find(function(c2) {
        return polygonContains(c2, pos)
      })
    })
  })
}


//
// Handler
//

function enter(country) {
  var country = countryList.find(function(c) {
    return c.id === country.id
  })
  current.text(country && country.name || '')
}

function leave(country) {
  current.text('')
}

function href(country) {
  console.log(country);
  var country = countryList.find(function(c){
      return c.id === country.id
  })
  window.open(country.name) //"https://google.com/" + 
}



function mousemove() {
  var c = getCountry(this)
  if (!c) {
    if (currentCountry) {
      leave(currentCountry)
      currentCountry = undefined
      render()
    }
    return
  }
  if (c === currentCountry) {
    return
  }
  currentCountry = c
  render()
  enter(c)
}

function mouseclick() {
  var c = getCountry(this)
  if (!c) {
    if (currentCountry) {
      leave(currentCountry)
      currentCountry = undefined
      render()
      
    }
    return
  }
  if (c === currentCountry) {
    href(c)
    return
  }
  currentCountry = c
  render()
}



canvas
  .call(d3.drag()
    .on('start', dragstarted)
    .on('drag', dragged)
    
    // .on('end', dragended)
   )
  .on('mousemove', mousemove)
  .on('click', mouseclick)

  loadData(function(world, cList) {
    land = topojson.feature(world, world.objects.land)
    countries = topojson.feature(world, world.objects.countries)
    countryList = cList
    
    window.addEventListener('resize', scale)
    scale()
    // autorotate = d3.timer(rotate)
  })