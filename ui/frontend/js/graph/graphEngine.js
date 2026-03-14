function initGraph(){
  const nodes = new vis.DataSet(GRAPH_DATA.nodes)
  const edges = new vis.DataSet(GRAPH_DATA.edges)

  AppState.nodes = nodes
  AppState.edges = edges

  const container = document.getElementById("graphCanvas")

  const network = new vis.Network(
    container,
    {nodes:nodes,edges:edges},
    {
      nodes:{
        borderWidth:2,
        borderWidthSelected:3,
        shape:"box",
        margin:8,
        color:{
          background:"#020617",
          border:"#60a5fa",
          highlight:{
            background:"#020617",
            border:"#38bdf8"
          },
          hover:{
            background:"#020617",
            border:"#93c5fd"
          }
        },
        font:{
          color:"#e5e7eb",
          face:"monospace",
          size:13
        }
      },
      layout:{
        improvedLayout:true
      },
      physics:{
        enabled:true,
        barnesHut:{
          gravitationalConstant:-7000,
          springLength:180,
          springConstant:0.04,
          damping:0.11
        },
        minVelocity:0.75
      },
      interaction:{
        dragView:true,
        zoomView:true,
        hover:true
      }
    }
  )

  AppState.graph = network

  // smooth initial fit
  network.once("stabilizationIterationsDone",function(){
    network.fit({animation:{duration:600,easing:"easeOutCubic"}})
  })

  // toolbar controls
  const btnCenter = document.getElementById("btn-center")
  const btnZoomIn = document.getElementById("btn-zoom-in")
  const btnZoomOut = document.getElementById("btn-zoom-out")

  if (btnCenter){
    btnCenter.onclick = function(){
      network.fit({animation:{duration:450,easing:"easeInOutQuad"}})
    }
  }

  function zoom(factor){
    const scale = network.getScale()
    network.moveTo({
      scale:scale*factor,
      animation:{duration:250,easing:"easeInOutQuad"}
    })
  }

  if (btnZoomIn){
    btnZoomIn.onclick = function(){ zoom(1.2) }
  }
  if (btnZoomOut){
    btnZoomOut.onclick = function(){ zoom(0.8) }
  }

  // node selection hooks for UML
  network.on("click",function(params){
    if (params.nodes && params.nodes.length){
      const id = params.nodes[0]
      AppState.selectedNode = id
      if (window.UML && typeof window.UML.showNodeDetails === "function"){
        window.UML.showNodeDetails(id)
      }
    }
  })

  network.on("hoverNode",function(params){
    if (window.UML && typeof window.UML.previewNode === "function"){
      window.UML.previewNode(params.node)
    }
  })

  network.on("blurNode",function(){
    if (window.UML && typeof window.UML.clearPreview === "function"){
      window.UML.clearPreview()
    }
  })
}