class SmartwatchSystem {
    constructor() {
      this.container = document.getElementById('container');
      this.pages = {};
      
      // Initialize variables for the stopwatch
      this.stopwatchRunning = false;
      this.stopwatchStartTime = null;
      this.stopwatchElapsed = 0;
      this.stopwatchInterval = null;
      
      // Initialize lap history
      this.lapHistory = [];
      this.loadLapHistory();
      
      // Create all pages
      this.createHomepage();
      this.createStopwatchPage();
      this.createWatchPage();
      
      // Start with the homepage
      this.showPage('homepage');
      
      // Start the clock update
      this.updateClock();
      setInterval(() => this.updateClock(), 1000);
    }
    
    createHomepage() {
      // Create homepage element
      const homepage = document.createElement('div');
      homepage.id = 'homepage';
      homepage.className = 'page';
      
      // Current time display
      const timeLabel = document.createElement('div');
      timeLabel.className = 'time-label';
      timeLabel.id = 'home-time';
      timeLabel.textContent = '12:00';
      homepage.appendChild(timeLabel);
      
      // Date display
      const dateLabel = document.createElement('div');
      dateLabel.className = 'date-label';
      dateLabel.id = 'home-date';
      dateLabel.textContent = 'Wed, Mar 5';
      homepage.appendChild(dateLabel);
      
      // App grid
      const appGrid = document.createElement('div');
      appGrid.className = 'app-grid';
      
      // Add app buttons
      appGrid.appendChild(this.createAppButton('⏱️', 'Stopwatch', () => this.showPage('stopwatch')));
      appGrid.appendChild(this.createAppButton('⌚', 'Watch', () => this.showPage('watch')));
      appGrid.appendChild(this.createAppButton('👣', 'Steps', () => this.showMessage('Steps counter will be available soon!')));
      appGrid.appendChild(this.createAppButton('⚙️', 'Settings', () => this.showMessage('Settings will be available soon!')));
      
      homepage.appendChild(appGrid);
      
      // Status bar
      const statusBar = document.createElement('div');
      statusBar.className = 'status-bar';
      statusBar.textContent = 'Battery: 85%';
      homepage.appendChild(statusBar);
      
      // Add to container and store reference
      this.container.appendChild(homepage);
      this.pages.homepage = homepage;
    }
    
    createStopwatchPage() {
      // Create stopwatch page
      const stopwatchPage = document.createElement('div');
      stopwatchPage.id = 'stopwatch';
      stopwatchPage.className = 'page';
      
      // Title bar with back button
      const titleBar = document.createElement('div');
      titleBar.className = 'title-bar';
      
      const backButton = document.createElement('button');
      backButton.className = 'back-button';
      backButton.textContent = '←';
      backButton.onclick = () => this.showPage('homepage');
      titleBar.appendChild(backButton);
      
      const title = document.createElement('div');
      title.className = 'title';
      title.textContent = 'Stopwatch';
      titleBar.appendChild(title);
      
      stopwatchPage.appendChild(titleBar);
      
      // Stopwatch display
      const stopwatchDisplay = document.createElement('div');
      stopwatchDisplay.className = 'stopwatch-display';
      stopwatchDisplay.id = 'stopwatch-display';
      stopwatchDisplay.textContent = '00:00.00';
      stopwatchPage.appendChild(stopwatchDisplay);
      
      // Lap display
      const lapDisplay = document.createElement('div');
      lapDisplay.className = 'lap-display';
      lapDisplay.id = 'lap-display';
      stopwatchPage.appendChild(lapDisplay);
      
      // View history button
      const viewHistoryButton = document.createElement('button');
      viewHistoryButton.textContent = 'View History';
      viewHistoryButton.className = 'control-button';
      viewHistoryButton.style.backgroundColor = '#9C27B0';
      viewHistoryButton.style.width = '100px';
      viewHistoryButton.style.marginBottom = '10px';
      viewHistoryButton.onclick = () => this.showLapHistoryModal();
      stopwatchPage.appendChild(viewHistoryButton);
      
      // Control buttons
      const controlButtons = document.createElement('div');
      controlButtons.className = 'control-buttons';
      
      const startStopButton = document.createElement('button');
      startStopButton.className = 'control-button start-button';
      startStopButton.id = 'start-stop-button';
      startStopButton.textContent = 'Start';
      startStopButton.onclick = () => this.toggleStopwatch();
      controlButtons.appendChild(startStopButton);
      
      const resetLapButton = document.createElement('button');
      resetLapButton.className = 'control-button lap-button disabled';
      resetLapButton.id = 'reset-lap-button';
      resetLapButton.textContent = 'Reset';
      resetLapButton.onclick = () => this.resetOrLap();
      controlButtons.appendChild(resetLapButton);
      
      stopwatchPage.appendChild(controlButtons);
      
      // Add to container and store reference
      this.container.appendChild(stopwatchPage);
      this.pages.stopwatch = stopwatchPage;
    }
    
    createWatchPage() {
      // Create watch page
      const watchPage = document.createElement('div');
      watchPage.id = 'watch';
      watchPage.className = 'page';
      
      // Title bar with back button
      const titleBar = document.createElement('div');
      titleBar.className = 'title-bar';
      
      const backButton = document.createElement('button');
      backButton.className = 'back-button';
      backButton.textContent = '←';
      backButton.onclick = () => this.showPage('homepage');
      titleBar.appendChild(backButton);
      
      const title = document.createElement('div');
      title.className = 'title';
      title.textContent = 'Watch';
      titleBar.appendChild(title);
      
      watchPage.appendChild(titleBar);
      
      // Time display
      const timeDisplay = document.createElement('div');
      timeDisplay.className = 'stopwatch-display';
      timeDisplay.id = 'watch-time';
      timeDisplay.textContent = '12:30';
      watchPage.appendChild(timeDisplay);
      
      // Date display
      const dateDisplay = document.createElement('div');
      dateDisplay.className = 'date-label';
      dateDisplay.id = 'watch-date';
      dateDisplay.textContent = 'Wed, Mar 5';
      watchPage.appendChild(dateDisplay);
      
      // Watch info
      const batteryInfo = document.createElement('div');
      batteryInfo.className = 'watch-info';
      batteryInfo.style.color = '#4CAF50';
      batteryInfo.textContent = 'Battery: 85%';
      watchPage.appendChild(batteryInfo);
      
      const stepsInfo = document.createElement('div');
      stepsInfo.className = 'watch-info';
      stepsInfo.style.color = '#2196F3';
      stepsInfo.textContent = 'Steps: 7,842';
      watchPage.appendChild(stepsInfo);
      
      // Add to container and store reference
      this.container.appendChild(watchPage);
      this.pages.watch = watchPage;
    }
    
    createAppButton(icon, label, clickHandler) {
      const button = document.createElement('button');
      button.className = 'app-button';
      button.onclick = clickHandler;
      
      const iconElement = document.createElement('div');
      iconElement.className = 'app-icon';
      iconElement.textContent = icon;
      button.appendChild(iconElement);
      
      const labelElement = document.createElement('div');
      labelElement.className = 'app-label';
      labelElement.textContent = label;
      button.appendChild(labelElement);
      
      return button;
    }
    
    showPage(pageName) {
      // Hide all pages
      Object.values(this.pages).forEach(page => {
        page.classList.remove('active');
      });
      
      // Show the selected page
      this.pages[pageName].classList.add('active');
      
      // If showing stopwatch page, update lap history display
      if (pageName === 'stopwatch') {
        this.updateLapHistoryDisplay();
      }
    }
    
    // Functions for persistent storage
    saveLapHistory() {
      localStorage.setItem('smartwatch_laps', JSON.stringify(this.lapHistory));
    }
    
    loadLapHistory() {
      try {
        const saved = localStorage.getItem('smartwatch_laps');
        this.lapHistory = saved ? JSON.parse(saved) : [];
      } catch (error) {
        console.error('Error loading lap history:', error);
        this.lapHistory = [];
      }
    }
    
    updateLapHistoryDisplay() {
      // Check if we have laps to display
      if (this.lapHistory.length === 0) return;
      
      const lapDisplay = document.getElementById('lap-display');
      
      // Show the most recent lap
      const recentLap = this.lapHistory[this.lapHistory.length - 1];
      lapDisplay.textContent = `Lap: ${recentLap.time}`;
      
      // Add a small indicator showing total saved laps
      const lapsCount = document.createElement('div');
      lapsCount.textContent = `${this.lapHistory.length} lap(s) saved`;
      lapsCount.style.fontSize = '10px';
      lapsCount.style.marginTop = '5px';
      lapsCount.style.color = '#888';
      
      // Replace any existing count element
      const existingCount = lapDisplay.querySelector('div');
      if (existingCount) {
        lapDisplay.removeChild(existingCount);
      }
      
      lapDisplay.appendChild(lapsCount);
    }
    
    updateClock() {
      const now = new Date();
      
      // Format strings
      const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', hour12: false });
      const dateStr = now.toLocaleDateString([], { weekday: 'short', month: 'short', day: 'numeric' });
      
      // Update homepage clock
      document.getElementById('home-time').textContent = timeStr;
      document.getElementById('home-date').textContent = dateStr;
      
      // Update watch page
      document.getElementById('watch-time').textContent = timeStr;
      document.getElementById('watch-date').textContent = dateStr;
    }
    
    toggleStopwatch() {
      const startStopButton = document.getElementById('start-stop-button');
      const resetLapButton = document.getElementById('reset-lap-button');
      
      if (!this.stopwatchRunning) {
        // Start the stopwatch
        this.stopwatchRunning = true;
        this.stopwatchStartTime = Date.now();
        startStopButton.textContent = 'Stop';
        startStopButton.classList.remove('start-button');
        startStopButton.classList.add('stop-button');
        resetLapButton.textContent = 'Lap';
        resetLapButton.classList.remove('disabled');
        
        // Start updating the display
        this.stopwatchInterval = setInterval(() => this.updateStopwatch(), 10); // Update every 10ms
      } else {
        // Stop the stopwatch
        this.stopwatchRunning = false;
        this.stopwatchElapsed += Date.now() - this.stopwatchStartTime;
        this.stopwatchStartTime = null;
        startStopButton.textContent = 'Start';
        startStopButton.classList.remove('stop-button');
        startStopButton.classList.add('start-button');
        resetLapButton.textContent = 'Reset';
        
        // Stop updating the display
        clearInterval(this.stopwatchInterval);
      }
    }
    
    updateStopwatch() {
      if (!this.stopwatchRunning) return;
      
      // Calculate current elapsed time
      let currentTime = this.stopwatchElapsed + (Date.now() - this.stopwatchStartTime);
      
      // Convert to minutes, seconds, centiseconds
      const minutes = Math.floor(currentTime / 60000);
      currentTime %= 60000;
      const seconds = Math.floor(currentTime / 1000);
      const centiseconds = Math.floor((currentTime % 1000) / 10);
      
      // Format and display
      document.getElementById('stopwatch-display').textContent = 
        `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}.${centiseconds.toString().padStart(2, '0')}`;
    }
    
    resetOrLap() {
      const resetLapButton = document.getElementById('reset-lap-button');
      const lapDisplay = document.getElementById('lap-display');
      
      if (this.stopwatchRunning) {
        // Record lap
        const currentTime = this.stopwatchElapsed + (Date.now() - this.stopwatchStartTime);
        const minutes = Math.floor(currentTime / 60000);
        const seconds = Math.floor((currentTime % 60000) / 1000);
        const centiseconds = Math.floor((currentTime % 1000) / 10);
        
        const lapTime = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}.${centiseconds.toString().padStart(2, '0')}`;
        lapDisplay.textContent = `Lap: ${lapTime}`;
        
        // Save lap to history with timestamp
        const lapData = {
          time: lapTime,
          timestamp: new Date().toISOString(),
          milliseconds: currentTime // Raw milliseconds for sorting
        };
        
        this.lapHistory.push(lapData);
        this.saveLapHistory();
      } else {
        // Reset the stopwatch
        this.stopwatchElapsed = 0;
        document.getElementById('stopwatch-display').textContent = "00:00.00";
        lapDisplay.textContent = "";
        resetLapButton.classList.add('disabled');
      }
    }
    
    showMessage(message, duration = 3000) {
      // Check if notification element exists, create it if not
      let messageNotification = document.getElementById('message-notification');
      if (!messageNotification) {
        messageNotification = document.createElement('div');
        messageNotification.id = 'message-notification';
        messageNotification.className = 'message-notification';
        this.container.appendChild(messageNotification);
      }
      
      // Show the message
      messageNotification.textContent = message;
      messageNotification.style.display = 'block';
      
      // Hide after duration
      setTimeout(() => {
        messageNotification.style.display = 'none';
      }, duration);
    }
    
    showLapHistoryModal() {
      // Create modal backdrop
      const backdrop = document.createElement('div');
      backdrop.style.position = 'absolute';
      backdrop.style.top = '0';
      backdrop.style.left = '0';
      backdrop.style.width = '100%';
      backdrop.style.height = '100%';
      backdrop.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
      backdrop.style.zIndex = '100';
      backdrop.style.display = 'flex';
      backdrop.style.flexDirection = 'column';
      backdrop.style.alignItems = 'center';
      backdrop.style.justifyContent = 'flex-start';
      backdrop.style.padding = '15px';
      backdrop.style.overflowY = 'auto';
      
      // Modal title
      const modalTitle = document.createElement('div');
      modalTitle.textContent = 'Lap History';
      modalTitle.style.fontSize = '18px';
      modalTitle.style.fontWeight = 'bold';
      modalTitle.style.marginBottom = '15px';
      modalTitle.style.color = 'white';
      backdrop.appendChild(modalTitle);
      
      // Create lap list
      const lapList = document.createElement('div');
      lapList.style.width = '100%';
      lapList.style.display = 'flex';
      lapList.style.flexDirection = 'column';
      lapList.style.gap = '8px';
      backdrop.appendChild(lapList);
      
      // Sort laps by date (most recent first)
      const sortedLaps = [...this.lapHistory].sort((a, b) => b.milliseconds - a.milliseconds);
      
      if (sortedLaps.length === 0) {
        const emptyMessage = document.createElement('div');
        emptyMessage.textContent = 'No laps recorded yet';
        emptyMessage.style.color = '#aaa';
        emptyMessage.style.textAlign = 'center';
        emptyMessage.style.marginTop = '20px';
        lapList.appendChild(emptyMessage);
      } else {
        // Add each lap to the list
        sortedLaps.forEach((lap, index) => {
          const lapItem = document.createElement('div');
          lapItem.style.backgroundColor = '#222';
          lapItem.style.padding = '8px';
          lapItem.style.borderRadius = '5px';
          lapItem.style.display = 'flex';
          lapItem.style.justifyContent = 'space-between';
          
          const lapNumber = document.createElement('span');
          lapNumber.textContent = `#${sortedLaps.length - index}`;
          lapNumber.style.color = '#aaa';
          lapItem.appendChild(lapNumber);
          
          const lapTime = document.createElement('span');
          lapTime.textContent = lap.time;
          lapTime.style.fontWeight = 'bold';
          lapItem.appendChild(lapTime);
          
          const lapDate = document.createElement('span');
          lapDate.textContent = new Date(lap.timestamp).toLocaleDateString();
          lapDate.style.color = '#aaa';
          lapDate.style.fontSize = '12px';
          lapItem.appendChild(lapDate);
          
          lapList.appendChild(lapItem);
        });
      }
      
      // Action buttons
      const buttonContainer = document.createElement('div');
      buttonContainer.style.display = 'flex';
      buttonContainer.style.justifyContent = 'space-between';
      buttonContainer.style.width = '100%';
      buttonContainer.style.marginTop = '15px';
      backdrop.appendChild(buttonContainer);
      
      // Close button
      const closeButton = document.createElement('button');
      closeButton.textContent = 'Close';
      closeButton.style.backgroundColor = '#2196F3';
      closeButton.style.color = 'white';
      closeButton.style.border = 'none';
      closeButton.style.padding = '8px 15px';
      closeButton.style.borderRadius = '5px';
      closeButton.style.fontWeight = 'bold';
      closeButton.onclick = () => {
        document.body.removeChild(backdrop);
      };
      buttonContainer.appendChild(closeButton);
      
      // Clear History button
      const clearButton = document.createElement('button');
      clearButton.textContent = 'Clear All';
      clearButton.style.backgroundColor = '#f44336';
      clearButton.style.color = 'white';
      clearButton.style.border = 'none';
      clearButton.style.padding = '8px 15px';
      clearButton.style.borderRadius = '5px';
      clearButton.style.fontWeight = 'bold';
      clearButton.onclick = () => {
        if (confirm('Are you sure you want to clear all lap history?')) {
          this.lapHistory = [];
          this.saveLapHistory();
          document.body.removeChild(backdrop);
          this.showMessage('Lap history cleared');
        }
      };
      buttonContainer.appendChild(clearButton);
      
      // Add the modal to the body
      document.body.appendChild(backdrop);
    }
  }
  
  // Initialize the application when the document is loaded
  document.addEventListener('DOMContentLoaded', () => {
    new SmartwatchSystem();
  });