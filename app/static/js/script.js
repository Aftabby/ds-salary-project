const config = { responsive: true }; // Enable responsiveness

document.addEventListener("DOMContentLoaded", () => {
  if (typeof graphData !== "undefined") {
    const modelPlotContainer = document.getElementById("graph3");
    const containerWidth = modelPlotContainer.offsetWidth;

    graphData[0].layout.width = 300;
    graphData[0].layout.height = 250;
    graphData[0].layout.legend = {
      orientation: "h",
      x: 0.5,
      xanchor: "center",
      y: -0.3, // Move legend further down
    };
    graphData[0].layout.margin = { l: 20, r: 20, t: 50, b: 30 }; // Reduce margins

    graphData[1].layout.width = 300;
    graphData[1].layout.height = 250;
    graphData[1].layout.legend = {
      orientation: "h",
      x: 0.5,
      xanchor: "center",
      y: -1, // Move legend further down
    };
    graphData[1].layout.margin = { l: 20, r: 20, t: 50, b: 30 }; // Reduce margins

    graphData[2].layout.width = containerWidth; // Set width to container's width
    graphData[2].layout.height = 250;
    graphData[2].layout.legend = {
      orientation: "h",
      x: 0.5,
      xanchor: "center",
      y: -0.7, // Move legend further down
    };
    graphData[2].layout.margin = { l: 20, r: 20, t: 50, b: 0 }; // Reduce margins

    Plotly.newPlot("graph1", graphData[0].data, graphData[0].layout);
    Plotly.newPlot("graph2", graphData[1].data, graphData[1].layout);
    Plotly.newPlot("graph3", graphData[2].data, graphData[2].layout);
  } else {
    console.error("Graph data is not defined or is empty.");
  }
});
