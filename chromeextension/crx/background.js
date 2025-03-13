const dwcNativePort = chrome.runtime.connectNative('ramune314159265.desktopwrapperchanger');

chrome.runtime.onMessageExternal.addListener(async (request, sender, sendResponse) => {
	console.log(request)
	switch (request.type) {
		case "desktop_color_change": {
			dwcNativePort.postMessage([...request.rgb])
			break
		}
		case "popup_focus": {
			const windows = await chrome.windows.getAll({ populate: true })
			const targetWindow = windows
				.filter(w => w.type === 'popup')
				.find(w => w.tabs.some(tab => tab.url.includes(request.id)))
			if (!targetWindow) {
				break
			}
			await chrome.windows.update(targetWindow.id, { focused: true })
			break
		}
		default:
			break
	}
})
