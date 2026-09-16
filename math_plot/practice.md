# 5-Day Matplotlib Curriculum for AI Students (Andrej Karpathy Companion)

Act as an expert AI mentor. I am a beginner learning deep learning from Andrej Karpathy's courses (like Neural Networks: Zero to Hero). I am struggling with the data visualization tools (`plt`) he uses to inspect models. Please act as my tutor and provide a comprehensive, 5-day step-by-step masterclass. 

For each of the 5 days below, provide a short, simple, hands-on Python tutorial (Jupyter Notebook style). Explain every line of code simply, tell me *why* Karpathy uses it in AI, and provide 1 small practice exercise at the end of each day.

---

### Day 1: Line Plots for Training Loss
Teach me how to visualize if an AI is learning over time.
1. Generate a mock list of "training losses" (numbers that decrease over time).
2. Plot them using `plt.plot()`.
3. Add a title, label the X-axis (Epochs/Iterations), and label the Y-axis (Loss).
4. Show me how to interpret a standard loss curve.

### Day 2: Image Show (imshow) for Grids and Weights
Teach me how to look inside the layers and datasets.
1. Create a simple 2D numpy array/tensor (like a 5x5 grid of random numbers).
2. Use `plt.imshow()` to display this grid as a colored heatmap.
3. Change the color palette using `cmap` (like 'Blues' or 'gray').
4. Add a colorbar (`plt.colorbar()`) to show what the colors mean numerically.
5. Explain how this applies to viewing image pixels or weight matrices.

### Day 3: Annotating Grids with Text (The Makemore Grid)
In Karpathy's bigram video, he builds a blue matrix containing character text and probabilities. Teach me the core mechanics:
1. Create a small 3x3 grid of numbers.
2. Display it using `plt.imshow()`.
3. Use a nested `for` loop to iterate through the rows and columns.
4. Use `plt.text()` to print the numerical values exactly inside each corresponding grid cell.
5. Explain the coordinate system (`x`, `y`) used by `plt.text()`.

### Day 4: Histograms for Activations and Gradients
Teach me how to check if my neural network layers are exploding or vanishing.
1. Generate a large distribution of random numbers (standard normal distribution).
2. Use `plt.hist()` to plot them as a histogram.
3. Change the number of `bins` to make the graph smoother or rougher.
4. Explain how to read this graph to check if weights are dead (all zero) or healthy.

### Day 5: Subplots for Comparing Data Side-by-Side
Teach me how to compare two metrics at once without overlapping them.
1. Use `plt.subplots(1, 2)` to create a side-by-side canvas layout.
2. Plot a line graph of "Loss" in the first subplot (left side).
3. Plot a line graph of "Accuracy" in the second subplot (right side).
4. Use `plt.tight_layout()` to clean up the spacing.
5. Explain how to select and control individual axes (`ax1`, `ax2`).
