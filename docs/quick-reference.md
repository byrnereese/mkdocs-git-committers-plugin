# RingCentral Office API Reference Index

Welcome to a simple index of RingCentral Office API endpoints, provided as a convenience for those who need a quick way to find a specific endpoint. For a complete reference, check out RingCentral's [complete and interactive Office API Reference](https://developer.ringcentral.com/api-reference).


### API Info

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        Get API Versions 
	
      </td>
      <td class="description"><p>Returns current API version(s) and server info.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi <a href="https://developers.ringcentral.com/api-reference/API-Info/readAPIVersions" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAPIVersions" class="collapse" aria-labelledby="readAPIVersions">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Version Info 
	
      </td>
      <td class="description"><p>Returns current API version info by apiVersion.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/{apiVersion} <a href="https://developers.ringcentral.com/api-reference/API-Info/readAPIVersion" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAPIVersion" class="collapse" aria-labelledby="readAPIVersion">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Service Status 
	
      </td>
      <td class="description"><p>Returns current PAS service status.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/status <a href="https://developers.ringcentral.com/api-reference/API-Info/readAPIStatus" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAPIStatus" class="collapse" aria-labelledby="readAPIStatus">
</div>
      </td>
    </tr>
</tbody>
</table>

### Automatic Location Updates

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listAutomaticLocationUpdatesUsers" aria-expanded="true" aria-controls="listAutomaticLocationUpdatesUsers">Get User List</a> 
        
      </td>
      <td class="description"><p>Returns the list of users with their status of Automatic Location Updates feature.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-address-auto-update/users <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/listAutomaticLocationUpdatesUsers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listAutomaticLocationUpdatesUsers" class="collapse" aria-labelledby="listAutomaticLocationUpdatesUsers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">department</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Department name to filter the users. The value range is 0-64; not case-sensitive. If not specified then the parameter is ignored. Multiple values are supported</td>
            </tr>
<tr>
	      <td class="n">featureEnabled</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Filters entries by their status of Automatic Location Updates feature</td>
            </tr>
<tr>
	      <td class="n">orderBy</td>
	      <td class="t">string</td>
	      <td class="d">name</td>
	      <td class="r">false</td>
	      <td class="de">Comma-separated list of fields to order results prefixed by plus sign '+' (ascending order) or minus sign '-' (descending order). Supported values: 'name', 'modelName', 'siteName', 'featureEnabled'</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are supported</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page</td>
            </tr>
<tr>
	      <td class="n">searchString</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Filters entries containing the specified substring in user name, extension or department. The characters range is 0-64; not case-sensitive. If empty then the filter is ignored</td>
            </tr>
<tr>
	      <td class="n">siteId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Internal identifier of a site. To filter users of Main Site (Company) `main-site` must be specified. Supported only If Multi-Site feature is enabled for the account. Multiple values are supported</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Extension type. Multiple values are supported</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#assignMultipleAutomaticaLocationUpdatesUsers" aria-expanded="true" aria-controls="assignMultipleAutomaticaLocationUpdatesUsers">Enable Automatic Location Updates for Users</a> 
        
      </td>
      <td class="description"><p>Enables or disables Automatic Location Updates feature for multiple account users.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/users/bulk-assign <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/assignMultipleAutomaticaLocationUpdatesUsers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="assignMultipleAutomaticaLocationUpdatesUsers" class="collapse" aria-labelledby="assignMultipleAutomaticaLocationUpdatesUsers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listWirelessPoints" aria-expanded="true" aria-controls="listWirelessPoints">Get Wireless Point List</a> 
        
      </td>
      <td class="description"><p>Returns account wireless points configured and used for Automatic Location Updates feature.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/listWirelessPoints" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listWirelessPoints" class="collapse" aria-labelledby="listWirelessPoints">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">orderBy</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Comma-separated list of fields to order results prefixed by '+' sign (ascending order) or '-' sign (descending order). The default sorting is by `name`</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are supported</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page</td>
            </tr>
<tr>
	      <td class="n">searchString</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Filters entries by the specified substring (search by chassis ID, switch name or address) The characters range is 0-64 (if empty the filter is ignored)</td>
            </tr>
<tr>
	      <td class="n">siteId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a site. To filter Main Site (Company) 'main-site' must be specified. Supported only If multi-site feature is enabled for the account</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createWirelessPoint" aria-expanded="true" aria-controls="createWirelessPoint">Create Wireless Point</a> 
        
      </td>
      <td class="description"><p>Creates a new wireless point in network configuration with the emergency address assigned.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/createWirelessPoint" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createWirelessPoint" class="collapse" aria-labelledby="createWirelessPoint">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readWirelessPoint" aria-expanded="true" aria-controls="readWirelessPoint">Get Wireless Point</a> 
        
      </td>
      <td class="description"><p>Returns the specified wireless access point of a corporate map with the emergency address assigned.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points/{pointId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/readWirelessPoint" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readWirelessPoint" class="collapse" aria-labelledby="readWirelessPoint">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">pointId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateWirelessPoint" aria-expanded="true" aria-controls="updateWirelessPoint">Update Wireless Point</a> 
        
      </td>
      <td class="description"><p>Updates the specified wireless access point of a corporate map by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points/{pointId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/updateWirelessPoint" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateWirelessPoint" class="collapse" aria-labelledby="updateWirelessPoint">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">pointId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteWirelessPoint" aria-expanded="true" aria-controls="deleteWirelessPoint">Delete Wireless Point</a> 
        
      </td>
      <td class="description"><p>Deletes wireless point(s) of a corporate map by ID(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points/{pointId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/deleteWirelessPoint" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteWirelessPoint" class="collapse" aria-labelledby="deleteWirelessPoint">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">pointId</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Network Map 
	
      </td>
      <td class="description"><p>Returns corporate networks map with emergency addresses assigned to the current account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/listNetworks" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listNetworks" class="collapse" aria-labelledby="listNetworks">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createNetwork" aria-expanded="true" aria-controls="createNetwork">Create Network</a> 
        
      </td>
      <td class="description"><p>Creates a new network in corporate ethernet map for assignment of emergency addresses to network access points.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/createNetwork" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createNetwork" class="collapse" aria-labelledby="createNetwork">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readNetwork" aria-expanded="true" aria-controls="readNetwork">Get Network</a> 
        
      </td>
      <td class="description"><p>Returns the specified network with emergency addresses assigned to the current account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks/{networkId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/readNetwork" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readNetwork" class="collapse" aria-labelledby="readNetwork">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">networkId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateNetwork" aria-expanded="true" aria-controls="updateNetwork">Update Network</a> 
        
      </td>
      <td class="description"><p>Updates network in corporate ethernet map for assignment of emergency addresses to network access points.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks/{networkId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/updateNetwork" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateNetwork" class="collapse" aria-labelledby="updateNetwork">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">networkId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteNetwork" aria-expanded="true" aria-controls="deleteNetwork">Delete Network</a> 
        
      </td>
      <td class="description"><p>Deletes network(s) in corporate ethernet map for Automatic Location Updates feature.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks/{networkId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/deleteNetwork" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteNetwork" class="collapse" aria-labelledby="deleteNetwork">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">networkId</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listDevicesAutomaticLocationUpdates" aria-expanded="true" aria-controls="listDevicesAutomaticLocationUpdates">Get Device List</a> 
        
      </td>
      <td class="description"><p>Returns the list of common devices with their status of Automatic Location Updates feature.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-address-auto-update/devices <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/listDevicesAutomaticLocationUpdates" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listDevicesAutomaticLocationUpdates" class="collapse" aria-labelledby="listDevicesAutomaticLocationUpdates">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">compatibleOnly</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Filters devices which support HELD protocol</td>
            </tr>
<tr>
	      <td class="n">featureEnabled</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Filters entries by their status of Automatic Location Updates feature</td>
            </tr>
<tr>
	      <td class="n">model</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Internal identifier of a device model for filtering. Multiple values are supported</td>
            </tr>
<tr>
	      <td class="n">orderBy</td>
	      <td class="t">string</td>
	      <td class="d">name</td>
	      <td class="r">false</td>
	      <td class="de">Comma-separated list of fields to order results prefixed by plus sign '+' (ascending order) or minus sign '-' (descending order). Supported values: 'name', 'modelName', 'siteName', 'featureEnabled'</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are supported</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page</td>
            </tr>
<tr>
	      <td class="n">searchString</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Filters entries which have device name or model name containing the mentioned substring. The value should be split by spaces; the range is 0 - 64 characters, not case-sensitive. If empty the filter is ignored</td>
            </tr>
<tr>
	      <td class="n">siteId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Internal identifier of a site. To filter devices of Main Site (Company) `main-site` must be specified. Supported only If Multi-Site feature is enabled for the account</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#assignMultipleDevicesAutomaticLocationUpdates" aria-expanded="true" aria-controls="assignMultipleDevicesAutomaticLocationUpdates">Enable Automatic Location Updates for Devices</a> 
        
      </td>
      <td class="description"><p>Enables or disables Automatic Location Updates feature for the specified common phones.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/devices/bulk-assign <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/assignMultipleDevicesAutomaticLocationUpdates" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="assignMultipleDevicesAutomaticLocationUpdates" class="collapse" aria-labelledby="assignMultipleDevicesAutomaticLocationUpdates">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listAccountSwitches" aria-expanded="true" aria-controls="listAccountSwitches">Get Account Switch List</a> 
        
      </td>
      <td class="description"><p>Returns corporate map of configured network switches with the assigned emergency addresses for the logged-in account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/listAccountSwitches" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listAccountSwitches" class="collapse" aria-labelledby="listAccountSwitches">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">orderBy</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Comma-separated list of fields to order results prefixed by '+' sign (ascending order) or '-' sign (descending order). The default sorting is by `name`</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are supported</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page</td>
            </tr>
<tr>
	      <td class="n">searchString</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Filters entries by the specified substring (search by chassis ID, switch name or address) The characters range is 0-64 (if empty the filter is ignored)</td>
            </tr>
<tr>
	      <td class="n">siteId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a site. To filter Main Site (Company) main-site must be specified. Supported only If multi-site feature is enabled for the account</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createSwitch" aria-expanded="true" aria-controls="createSwitch">Create Switch</a> 
        
      </td>
      <td class="description"><p>Creates a new switch in corporate map based on chassis ID and used for Automatic Locations Update feature.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/createSwitch" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createSwitch" class="collapse" aria-labelledby="createSwitch">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readSwitch" aria-expanded="true" aria-controls="readSwitch">Get Switch</a> 
        
      </td>
      <td class="description"><p>Returns the specified switch with the assigned emergency address.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches/{switchId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/readSwitch" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readSwitch" class="collapse" aria-labelledby="readSwitch">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">switchId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateSwitch" aria-expanded="true" aria-controls="updateSwitch">Update Switch</a> 
        
      </td>
      <td class="description"><p>Updates switch. Partial update is not supported, all switch parameters should be specified. If null value is received or parameter is missing, its value is removed.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches/{switchId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/updateSwitch" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateSwitch" class="collapse" aria-labelledby="updateSwitch">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">switchId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteSwitch" aria-expanded="true" aria-controls="deleteSwitch">Delete Switch</a> 
        
      </td>
      <td class="description"><p>Deletes wireless switch(es) in network configuration for Automatic Location Updates feature.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches/{switchId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/deleteSwitch" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteSwitch" class="collapse" aria-labelledby="deleteSwitch">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">switchId</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createMultipleSwitches" aria-expanded="true" aria-controls="createMultipleSwitches">Create Multiple Switches</a> 
        
      </td>
      <td class="description"><p>Creates multiple switches in corporate map. The maximum number of switches per request is 10 000; limitation for account is 10 000.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches-bulk-create <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/createMultipleSwitches" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createMultipleSwitches" class="collapse" aria-labelledby="createMultipleSwitches">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateMultipleSwitches" aria-expanded="true" aria-controls="updateMultipleSwitches">Update Multiple Switches</a> 
        
      </td>
      <td class="description"><p>Updates multiple switches in corporate map. The maximum number of switches per request is 10 000; limitation for account is 10 000.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches-bulk-update <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/updateMultipleSwitches" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateMultipleSwitches" class="collapse" aria-labelledby="updateMultipleSwitches">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createMultipleWirelessPoints" aria-expanded="true" aria-controls="createMultipleWirelessPoints">Create Multiple Wireless Points</a> 
        
      </td>
      <td class="description"><p>Creates multiple wireless points in corporate map. The maximum number of wireless points per request is 10 000; limitation for account is 70 000.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points-bulk-create <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/createMultipleWirelessPoints" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createMultipleWirelessPoints" class="collapse" aria-labelledby="createMultipleWirelessPoints">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateMultipleWirelessPoints" aria-expanded="true" aria-controls="updateMultipleWirelessPoints">Update Multiple Wireless Points</a> 
        
      </td>
      <td class="description"><p>Updates wireless points in corporate map. The maximum number of wireless points per request is 10 000; limitation for account is 70 000.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points-bulk-update <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/updateMultipleWirelessPoints" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateMultipleWirelessPoints" class="collapse" aria-labelledby="updateMultipleWirelessPoints">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#validateMultipleWirelessPoints" aria-expanded="true" aria-controls="validateMultipleWirelessPoints">Validate Multiple Wireless Points</a> 
        
      </td>
      <td class="description"><p>Validates wireless points before creation or update. The maximum number of wireless points per request is 10 000.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points-bulk-validate <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/validateMultipleWirelessPoints" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="validateMultipleWirelessPoints" class="collapse" aria-labelledby="validateMultipleWirelessPoints">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#validateMultipleSwitches" aria-expanded="true" aria-controls="validateMultipleSwitches">Validate Multiple Switches</a> 
        
      </td>
      <td class="description"><p>Validates switches before creation or update. The maximum number of switches per request is 10 000.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches-bulk-validate <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/validateMultipleSwitches" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="validateMultipleSwitches" class="collapse" aria-labelledby="validateMultipleSwitches">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readAutomaticLocationUpdatesTask" aria-expanded="true" aria-controls="readAutomaticLocationUpdatesTask">Get Emergency Map Configuration Task</a> 
        
      </td>
      <td class="description"><p>Returns results of the task created within the frame of Automatic Location Updates feature. Currently four task types are supported: 'Wireless Points Bulk Create', 'Wireless Points Bulk Update', 'Switches Bulk Create', 'Switches Bulk Update'</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-address-auto-update/tasks/{taskId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/readAutomaticLocationUpdatesTask" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAutomaticLocationUpdatesTask" class="collapse" aria-labelledby="readAutomaticLocationUpdatesTask">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">taskId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createEmergencyLocation" aria-expanded="true" aria-controls="createEmergencyLocation">Add Emergency Location</a> 
        
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/emergency-locations <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/createEmergencyLocation" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createEmergencyLocation" class="collapse" aria-labelledby="createEmergencyLocation">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listEmergencyLocations" aria-expanded="true" aria-controls="listEmergencyLocations">Get Emergency Location List</a> 
        
      </td>
      <td class="description"><p>Returns emergency response locations of the current account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-locations <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/listEmergencyLocations" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listEmergencyLocations" class="collapse" aria-labelledby="listEmergencyLocations">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">addressStatus</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">domesticCountryId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">orderBy</td>
	      <td class="t">string</td>
	      <td class="d">address</td>
	      <td class="r">false</td>
	      <td class="de">Comma-separated list of fields to order results prefixed by plus sign '+' (ascending order) or minus sign '-' (descending order). Supported values: 'address'</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are supported</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Indicates the page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page</td>
            </tr>
<tr>
	      <td class="n">searchString</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Filters entries containing the specified substring in address and name fields. The characters range is 0-64; not case-sensitive. If empty then the filter is ignored</td>
            </tr>
<tr>
	      <td class="n">siteId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Internal identifier of a site for filtering. To filter by Main Site (Company) `main-site` value should be specified</td>
            </tr>
<tr>
	      <td class="n">usageStatus</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readEmergencyLocation" aria-expanded="true" aria-controls="readEmergencyLocation">Get Emergency Location</a> 
        
      </td>
      <td class="description"><p>Returns emergency response location by ID</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/emergency-locations/{locationId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/readEmergencyLocation" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readEmergencyLocation" class="collapse" aria-labelledby="readEmergencyLocation">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">locationId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of the emergency location</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateEmergencyLocation" aria-expanded="true" aria-controls="updateEmergencyLocation">Update Emergency Location</a> 
        
      </td>
      <td class="description"><p>Updates the specified emergency response location.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/emergency-locations/{locationId} <a href="https://developers.ringcentral.com/api-reference/Automatic-Location-Updates/updateEmergencyLocation" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateEmergencyLocation" class="collapse" aria-labelledby="updateEmergencyLocation">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">locationId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of the emergency location</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Business Hours

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readUserBusinessHours" aria-expanded="true" aria-controls="readUserBusinessHours">Get User Business Hours</a> 
        
      </td>
      <td class="description"><p>Returns the user hours when the call handling rules are applied. <strong>Please note:</strong> If user hours are set to 'Custom hours' then a particular schedule is returned; however if set to '24 hours/7 days a week' an empty schedule is returned.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/business-hours <a href="https://developers.ringcentral.com/api-reference/Business-Hours/readUserBusinessHours" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUserBusinessHours" class="collapse" aria-labelledby="readUserBusinessHours">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateUserBusinessHours" aria-expanded="true" aria-controls="updateUserBusinessHours">Update User Business Hours</a> 
        
      </td>
      <td class="description"><p>Updates the extension user hours when answering rules are to be applied.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/business-hours <a href="https://developers.ringcentral.com/api-reference/Business-Hours/updateUserBusinessHours" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateUserBusinessHours" class="collapse" aria-labelledby="updateUserBusinessHours">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Company Business Hours 
	
      </td>
      <td class="description"><p>Returns company hours when answering rules are to be applied.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/business-hours <a href="https://developers.ringcentral.com/api-reference/Business-Hours/readCompanyBusinessHours" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCompanyBusinessHours" class="collapse" aria-labelledby="readCompanyBusinessHours">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateCompanyBusinessHours" aria-expanded="true" aria-controls="updateCompanyBusinessHours">Update Company Business Hours</a> 
        
      </td>
      <td class="description"><p>Updates company hours when answering rules are to be applied.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/business-hours <a href="https://developers.ringcentral.com/api-reference/Business-Hours/updateCompanyBusinessHours" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateCompanyBusinessHours" class="collapse" aria-labelledby="updateCompanyBusinessHours">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Calendar Events

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readGlipEvents" aria-expanded="true" aria-controls="readGlipEvents">Get User Events List</a> 
        
      </td>
      <td class="description"><p>Returns all calendar events created by the current user.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/events <a href="https://developers.ringcentral.com/api-reference/Calendar-Events/readGlipEvents" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipEvents" class="collapse" aria-labelledby="readGlipEvents">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Token of a page to be returned</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Number of groups to be fetched by one request. The maximum value is 250, by default - 30.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Create Event 
	
      </td>
      <td class="description"><p>Creates a new calendar event.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/events <a href="https://developers.ringcentral.com/api-reference/Calendar-Events/createEvent" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createEvent" class="collapse" aria-labelledby="createEvent">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Event 
	
      </td>
      <td class="description"><p>Returns the specified calendar event(s) by ID(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/events/{eventId} <a href="https://developers.ringcentral.com/api-reference/Calendar-Events/readEvent" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readEvent" class="collapse" aria-labelledby="readEvent">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateEvent" aria-expanded="true" aria-controls="updateEvent">Update Event</a> 
        
      </td>
      <td class="description"><p>Updates the specified calendar event.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/glip/events/{eventId} <a href="https://developers.ringcentral.com/api-reference/Calendar-Events/updateEvent" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateEvent" class="collapse" aria-labelledby="updateEvent">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">eventId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an event</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Delete Event 
	
      </td>
      <td class="description"><p>Deletes the specified calendar event.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/glip/events/{eventId} <a href="https://developers.ringcentral.com/api-reference/Calendar-Events/deleteEvent" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteEvent" class="collapse" aria-labelledby="deleteEvent">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createEventbyGroupId" aria-expanded="true" aria-controls="createEventbyGroupId">Create Event by Group ID</a> 
        
      </td>
      <td class="description"><p>Creates a new calendar event within the specified group.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/groups/{groupId}/events <a href="https://developers.ringcentral.com/api-reference/Calendar-Events/createEventbyGroupId" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createEventbyGroupId" class="collapse" aria-labelledby="createEventbyGroupId">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a group</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Group Events 
	
      </td>
      <td class="description"><p>Returns a list of calendar events available for the current user within the specified group. Users can only see their personal tasks and public tasks.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/groups/{groupId}/events <a href="https://developers.ringcentral.com/api-reference/Calendar-Events/listGroupEvents" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listGroupEvents" class="collapse" aria-labelledby="listGroupEvents">
</div>
      </td>
    </tr>
</tbody>
</table>

### Call Blocking

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readCallerBlockingSettings" aria-expanded="true" aria-controls="readCallerBlockingSettings">Get Caller Blocking Settings</a> 
        
      </td>
      <td class="description"><p>Returns the current caller blocking settings of a user.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking <a href="https://developers.ringcentral.com/api-reference/Call-Blocking/readCallerBlockingSettings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCallerBlockingSettings" class="collapse" aria-labelledby="readCallerBlockingSettings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateCallerBlockingSettings" aria-expanded="true" aria-controls="updateCallerBlockingSettings">Update Caller Blocking Settings</a> 
        
      </td>
      <td class="description"><p>Updates the current caller blocking settings of a user.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking <a href="https://developers.ringcentral.com/api-reference/Call-Blocking/updateCallerBlockingSettings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateCallerBlockingSettings" class="collapse" aria-labelledby="updateCallerBlockingSettings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listBlockedAllowedNumbers" aria-expanded="true" aria-controls="listBlockedAllowedNumbers">Get Blocked/Allowed Phone Numbers</a> 
        
      </td>
      <td class="description"><p>Returns the lists of blocked and allowed phone numbers.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers <a href="https://developers.ringcentral.com/api-reference/Call-Blocking/listBlockedAllowedNumbers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listBlockedAllowedNumbers" class="collapse" aria-labelledby="listBlockedAllowedNumbers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">status</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createBlockedAllowedNumber" aria-expanded="true" aria-controls="createBlockedAllowedNumber">Add Blocked/Allowed Number</a> 
        
      </td>
      <td class="description"><p>Updates either blocked or allowed phone number list with a new phone number.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers <a href="https://developers.ringcentral.com/api-reference/Call-Blocking/createBlockedAllowedNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createBlockedAllowedNumber" class="collapse" aria-labelledby="createBlockedAllowedNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readBlockedAllowedNumber" aria-expanded="true" aria-controls="readBlockedAllowedNumber">Get Blocked/Allowed Number</a> 
        
      </td>
      <td class="description"><p>Returns blocked or allowed phone number(s) by their ID(s). Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers/{blockedNumberId} <a href="https://developers.ringcentral.com/api-reference/Call-Blocking/readBlockedAllowedNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readBlockedAllowedNumber" class="collapse" aria-labelledby="readBlockedAllowedNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">blockedNumberId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteBlockedAllowedNumber" aria-expanded="true" aria-controls="deleteBlockedAllowedNumber">Delete Blocked/Allowed Number</a> 
        
      </td>
      <td class="description"><p>Deletes blocked or allowed phone number(s) by their ID(s). Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers/{blockedNumberId} <a href="https://developers.ringcentral.com/api-reference/Call-Blocking/deleteBlockedAllowedNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteBlockedAllowedNumber" class="collapse" aria-labelledby="deleteBlockedAllowedNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">blockedNumberId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateBlockedAllowedNumber" aria-expanded="true" aria-controls="updateBlockedAllowedNumber">Update Blocked/Allowed Number</a> 
        
      </td>
      <td class="description"><p>Updates blocked or allowed phone number(s) by their ID(s). Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers/{blockedNumberId} <a href="https://developers.ringcentral.com/api-reference/Call-Blocking/updateBlockedAllowedNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateBlockedAllowedNumber" class="collapse" aria-labelledby="updateBlockedAllowedNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">blockedNumberId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Call Control

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createCallOutCallSession" aria-expanded="true" aria-controls="createCallOutCallSession">Make CallOut</a> 
        
      </td>
      <td class="description"><p>Creates a new outbound call out session.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/call-out <a href="https://developers.ringcentral.com/api-reference/Call-Control/createCallOutCallSession" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createCallOutCallSession" class="collapse" aria-labelledby="createCallOutCallSession">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readCallSessionStatus" aria-expanded="true" aria-controls="readCallSessionStatus">Get Call Session Status</a> 
        
      </td>
      <td class="description"><p>Returns the status of a call session by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId} <a href="https://developers.ringcentral.com/api-reference/Call-Control/readCallSessionStatus" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCallSessionStatus" class="collapse" aria-labelledby="readCallSessionStatus">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
<tr>
	      <td class="n">timeout</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The time frame of awaiting for a status change before sending the resulting one in response</td>
            </tr>
<tr>
	      <td class="n">timestamp</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The date and time of a call session latest change</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteCallSession" aria-expanded="true" aria-controls="deleteCallSession">Drop Call Session</a> 
        
      </td>
      <td class="description"><p>Drops a call session.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId} <a href="https://developers.ringcentral.com/api-reference/Call-Control/deleteCallSession" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteCallSession" class="collapse" aria-labelledby="deleteCallSession">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#holdCallParty" aria-expanded="true" aria-controls="holdCallParty">Hold Call Party</a> 
        
      </td>
      <td class="description"><p>Puts the party to stand-alone mode and starts to play Hold Music according to configuration &amp; state to peers. There is a known limitation for Hold API - hold via REST API doesn't work with hold placed via RingCentral apps or HardPhone. It means that if you muted participant via Call Control API and RingCentral Desktop app, then you need to unhold both endpoints to remove Hold Music and bring media back.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/hold <a href="https://developers.ringcentral.com/api-reference/Call-Control/holdCallParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="holdCallParty" class="collapse" aria-labelledby="holdCallParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#unholdCallParty" aria-expanded="true" aria-controls="unholdCallParty">Unhold Call Party</a> 
        
      </td>
      <td class="description"><p>Brings a party back into a call and stops to play Hold Music. There is a known limitation for Hold API - hold via REST API doesn't work with hold placed via RingCentral apps or HardPhone. It means that if you muted participant via Call Control API and RingCentral Desktop app, then you need to unhold both endpoints to remove Hold Music and bring media back.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/unhold <a href="https://developers.ringcentral.com/api-reference/Call-Control/unholdCallParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="unholdCallParty" class="collapse" aria-labelledby="unholdCallParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#rejectParty" aria-expanded="true" aria-controls="rejectParty">Reject Call Party</a> 
        
      </td>
      <td class="description"><p>Rejects an inbound call in a "Setup" or "Proceeding" state</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/reject <a href="https://developers.ringcentral.com/api-reference/Call-Control/rejectParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="rejectParty" class="collapse" aria-labelledby="rejectParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#ignoreCallInQueue" aria-expanded="true" aria-controls="ignoreCallInQueue">Ignore Call in Queue</a> 
        
      </td>
      <td class="description"><p>Ignores a call to a call queue agent in <code>Setup</code> or <code>Proceeding</code> state.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/ignore <a href="https://developers.ringcentral.com/api-reference/Call-Control/ignoreCallInQueue" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="ignoreCallInQueue" class="collapse" aria-labelledby="ignoreCallInQueue">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#transferCallParty" aria-expanded="true" aria-controls="transferCallParty">Transfer Call Party</a> 
        
      </td>
      <td class="description"><p>Transfers a party by placing a new call to the specified target</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/transfer <a href="https://developers.ringcentral.com/api-reference/Call-Control/transferCallParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="transferCallParty" class="collapse" aria-labelledby="transferCallParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Defines a target for a party transfer. Only a single target is allowed</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#answerCallParty" aria-expanded="true" aria-controls="answerCallParty">Answer Call Party</a> 
        
      </td>
      <td class="description"><p>Answers a call on a certain device using this device identifier. Currently it is possible to answer an incoming call via this method after the following actions: call forward, call transfer or call flip.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/answer <a href="https://developers.ringcentral.com/api-reference/Call-Control/answerCallParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="answerCallParty" class="collapse" aria-labelledby="answerCallParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Distributes a non-answered call to the defined target. Only a single target is allowed</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#pickupCallParty" aria-expanded="true" aria-controls="pickupCallParty">Pickup Call</a> 
        
      </td>
      <td class="description"><p>Picks up a call parked to the specified park location.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/pickup <a href="https://developers.ringcentral.com/api-reference/Call-Control/pickupCallParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="pickupCallParty" class="collapse" aria-labelledby="pickupCallParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Distributes a non-answered call to the defined target. Only a single target is allowed</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#forwardCallParty" aria-expanded="true" aria-controls="forwardCallParty">Forward Call Party</a> 
        
      </td>
      <td class="description"><p>Distributes a non-answered call to the defined target. Applicable for "Setup" or "Proceeding" states</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/forward <a href="https://developers.ringcentral.com/api-reference/Call-Control/forwardCallParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="forwardCallParty" class="collapse" aria-labelledby="forwardCallParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Distributes a non-answered call to the defined target. Only a single target is allowed</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#replyParty" aria-expanded="true" aria-controls="replyParty">Reply with Text</a> 
        
      </td>
      <td class="description"><p>Replies with text/pattern without picking up a call.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/reply <a href="https://developers.ringcentral.com/api-reference/Call-Control/replyParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="replyParty" class="collapse" aria-labelledby="replyParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#callFlipParty" aria-expanded="true" aria-controls="callFlipParty">Call Flip on Party</a> 
        
      </td>
      <td class="description"><p>Performs call flip procedure by holding opposite party and calling to the specified target</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/flip <a href="https://developers.ringcentral.com/api-reference/Call-Control/callFlipParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="callFlipParty" class="collapse" aria-labelledby="callFlipParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#callParkParty" aria-expanded="true" aria-controls="callParkParty">Call Park</a> 
        
      </td>
      <td class="description"><p>Parks a call to a virtual location from where it can further be retrieved by any user from any phone of the system. The call session and call party identifiers should be specified in path. Currently the users can park only their own incoming calls. Up to 50 calls can be parked simultaneously. Park location starts with asterisk (*) and ranges 801-899.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/park <a href="https://developers.ringcentral.com/api-reference/Call-Control/callParkParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="callParkParty" class="collapse" aria-labelledby="callParkParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readCallPartyStatus" aria-expanded="true" aria-controls="readCallPartyStatus">Get Call Party Status</a> 
        
      </td>
      <td class="description"><p>Returns a party status of a call session by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId} <a href="https://developers.ringcentral.com/api-reference/Call-Control/readCallPartyStatus" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCallPartyStatus" class="collapse" aria-labelledby="readCallPartyStatus">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateCallParty" aria-expanded="true" aria-controls="updateCallParty">Update Call Party</a> 
        
      </td>
      <td class="description"><p>Modify the party of a call session by ID. There is a known limitation for Mute scenario - mute via REST API doesn't work with mute placed via RingCentral apps or HardPhone. It means that if you muted participant via Call Control API and Ringcentral Desktop app you need to unmute both endpoints to bring media back. </p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId} <a href="https://developers.ringcentral.com/api-reference/Call-Control/updateCallParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateCallParty" class="collapse" aria-labelledby="updateCallParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#startCallRecording" aria-expanded="true" aria-controls="startCallRecording">Create Recording</a> 
        
      </td>
      <td class="description"><p>Starts a new call recording for the party</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/recordings <a href="https://developers.ringcentral.com/api-reference/Call-Control/startCallRecording" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="startCallRecording" class="collapse" aria-labelledby="startCallRecording">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#pauseResumeCallRecording" aria-expanded="true" aria-controls="pauseResumeCallRecording">Pause/Resume Recording</a> 
        
      </td>
      <td class="description"><p>Pause/resume recording</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/recordings/{recordingId} <a href="https://developers.ringcentral.com/api-reference/Call-Control/pauseResumeCallRecording" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="pauseResumeCallRecording" class="collapse" aria-labelledby="pauseResumeCallRecording">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">brandId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Identifies a brand of a logged in user or a brand of a sign-up session</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">recordingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a recording</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#superviseCallSession" aria-expanded="true" aria-controls="superviseCallSession">Supervise Call Session</a> 
        
      </td>
      <td class="description"><p>Allows to monitor a call session in 'Listen' mode. Input parameters should contain internal identifiers of a monitored user and a supervisor's device. Call session should be specified in path. Please note that this method supports single channel audio flow, which means that audio of both call participants is mixed and delivered to the supervisor in single audio channel.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/supervise <a href="https://developers.ringcentral.com/api-reference/Call-Control/superviseCallSession" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="superviseCallSession" class="collapse" aria-labelledby="superviseCallSession">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#superviseCallParty" aria-expanded="true" aria-controls="superviseCallParty">Supervise Call Party</a> 
        
      </td>
      <td class="description"><p>Allows to monitor a call party in 'Listen' mode. Input parameters are extension number of a monitored user and internal identifier of a supervisor's device. Call session and party identifiers should be specified in path. Please note that for this method dual channel audio flow is supported, which means that you need to make one more request for monitoring the second participant of a call. And as a result of each monitoring request the client recieves SIP invite with the following header <code>p-rc-api-monitoring-ids</code> containing IDs of the monitored party and session. The flow is supported for calls with no more than 2 participants.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/supervise <a href="https://developers.ringcentral.com/api-reference/Call-Control/superviseCallParty" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="superviseCallParty" class="collapse" aria-labelledby="superviseCallParty">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">partyId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call party</td>
            </tr>
<tr>
	      <td class="n">telephonySessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Call Forwarding

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listForwardingNumbers" aria-expanded="true" aria-controls="listForwardingNumbers">Get Forwarding Number List</a> 
        
      </td>
      <td class="description"><p>Returns the list of extension phone numbers used for call forwarding and call flip. The returned list contains all the extension phone numbers used for call forwarding and call flip.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number <a href="https://developers.ringcentral.com/api-reference/Call-Forwarding/listForwardingNumbers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listForwardingNumbers" class="collapse" aria-labelledby="listForwardingNumbers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted.</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items).</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createForwardingNumber" aria-expanded="true" aria-controls="createForwardingNumber">Create Forwarding Number</a> 
        
      </td>
      <td class="description"><p>Adds a new forwarding number to the forwarding number list.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number <a href="https://developers.ringcentral.com/api-reference/Call-Forwarding/createForwardingNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createForwardingNumber" class="collapse" aria-labelledby="createForwardingNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readForwardingNumber" aria-expanded="true" aria-controls="readForwardingNumber">Get Forwarding Number</a> 
        
      </td>
      <td class="description"><p>Returns a specific forwarding number.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number/{forwardingNumberId} <a href="https://developers.ringcentral.com/api-reference/Call-Forwarding/readForwardingNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readForwardingNumber" class="collapse" aria-labelledby="readForwardingNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">forwardingNumberId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateForwardingNumber" aria-expanded="true" aria-controls="updateForwardingNumber">Update Forwarding Number</a> 
        
      </td>
      <td class="description"><p>Updates the existing forwarding number from the forwarding number list.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number/{forwardingNumberId} <a href="https://developers.ringcentral.com/api-reference/Call-Forwarding/updateForwardingNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateForwardingNumber" class="collapse" aria-labelledby="updateForwardingNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">forwardingNumberId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a forwarding number; returned in response in the 'id' field</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteForwardingNumber" aria-expanded="true" aria-controls="deleteForwardingNumber">Delete Forwarding Number</a> 
        
      </td>
      <td class="description"><p>Deletes a forwarding number from the forwarding number list by its ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number/{forwardingNumberId} <a href="https://developers.ringcentral.com/api-reference/Call-Forwarding/deleteForwardingNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteForwardingNumber" class="collapse" aria-labelledby="deleteForwardingNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">forwardingNumberId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a forwarding number</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Call Log

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readUserCallLog" aria-expanded="true" aria-controls="readUserCallLog">Get User Call Log Records</a> 
        
      </td>
      <td class="description"><p>Returns call log records filtered by parameters specified.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/call-log <a href="https://developers.ringcentral.com/api-reference/Call-Log/readUserCallLog" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUserCallLog" class="collapse" aria-labelledby="readUserCallLog">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">dateFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The start datetime for resulting records in (ISO 8601)[https://en.wikipedia.org/wiki/ISO_8601] format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is dateTo minus 24 hours</td>
            </tr>
<tr>
	      <td class="n">dateTo</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The end datetime for resulting records in (ISO 8601)[https://en.wikipedia.org/wiki/ISO_8601] format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is current time</td>
            </tr>
<tr>
	      <td class="n">direction</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The direction for the resulting records. If not specified, both inbound and outbound records are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionNumber</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Extension number of a user. If specified, returns call log for a particular extension only</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are allowed</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">phoneNumber</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Phone number of a caller/callee. If specified, returns all calls (both incoming and outcoming) with the phone number specified</td>
            </tr>
<tr>
	      <td class="n">recordingType</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Type of a call recording. If not specified, then calls without recordings are also returned</td>
            </tr>
<tr>
	      <td class="n">sessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a session</td>
            </tr>
<tr>
	      <td class="n">showBlocked</td>
	      <td class="t">boolean</td>
	      <td class="d">True</td>
	      <td class="r">False</td>
	      <td class="de">If 'True' then calls from/to blocked numbers are returned</td>
            </tr>
<tr>
	      <td class="n">showDeleted</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">False</td>
	      <td class="de">If 'True' then deleted calls are returned</td>
            </tr>
<tr>
	      <td class="n">transport</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Call transport type. 'PSTN' specifies that a call leg is initiated from the PSTN network provider; 'VoIP' - from an RC phone. By default this filter is disabled</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Call type of a record. It is allowed to specify more than one type. If not specified, all call types are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">view</td>
	      <td class="t">string</td>
	      <td class="d">Simple</td>
	      <td class="r">False</td>
	      <td class="de">View of call records. The same view parameter specified for FSync will be applied for ISync, the view cannot be changed for ISync</td>
            </tr>
<tr>
	      <td class="n">withRecording</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">False</td>
	      <td class="de">**Deprecated**. Supported for compatibility reasons. `True` if only recorded calls are returned. If both `withRecording` and `recordingType` are specified, then `withRecording` is ignored</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteUserCallLog" aria-expanded="true" aria-controls="deleteUserCallLog">Delete User Call Log</a> 
        
      </td>
      <td class="description"><p>Deletes filtered call log records.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/call-log <a href="https://developers.ringcentral.com/api-reference/Call-Log/deleteUserCallLog" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteUserCallLog" class="collapse" aria-labelledby="deleteUserCallLog">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">dateFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">dateTo</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The end datetime for records deletion in (ISO 8601)[https://en.wikipedia.org/wiki/ISO_8601]  format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is current time</td>
            </tr>
<tr>
	      <td class="n">direction</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionNumber</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">phoneNumber</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#syncUserCallLog" aria-expanded="true" aria-controls="syncUserCallLog">Sync User Call Log</a> 
        
      </td>
      <td class="description"><p>Synchronizes call log records</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/call-log-sync <a href="https://developers.ringcentral.com/api-reference/Call-Log/syncUserCallLog" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="syncUserCallLog" class="collapse" aria-labelledby="syncUserCallLog">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">dateFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The start datetime for resulting records in (ISO 8601)[https://en.wikipedia.org/wiki/ISO_8601] format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is the current moment</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">For 'FSync' the parameter is mandatory, it limits the number of records to be returned in response. For 'ISync' it specifies with how many records to extend sync Frame to the past, the maximum number of records is 250</td>
            </tr>
<tr>
	      <td class="n">showDeleted</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">False</td>
	      <td class="de">Supported for ISync. If 'True' then deleted call records are returned</td>
            </tr>
<tr>
	      <td class="n">statusGroup</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of calls to be returned. The default value is 'All'</td>
            </tr>
<tr>
	      <td class="n">syncToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Value of syncToken property of last sync request response</td>
            </tr>
<tr>
	      <td class="n">syncType</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of synchronization</td>
            </tr>
<tr>
	      <td class="n">view</td>
	      <td class="t">string</td>
	      <td class="d">Simple</td>
	      <td class="r">False</td>
	      <td class="de">View of call records. The same view parameter specified for FSync will be applied for ISync, the view cannot be changed for ISync</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readUserCallRecord" aria-expanded="true" aria-controls="readUserCallRecord">Get User Call Record</a> 
        
      </td>
      <td class="description"><p>Returns call log records by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/call-log/{callRecordId} <a href="https://developers.ringcentral.com/api-reference/Call-Log/readUserCallRecord" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUserCallRecord" class="collapse" aria-labelledby="readUserCallRecord">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">callRecordId</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">view</td>
	      <td class="t">string</td>
	      <td class="d">Simple</td>
	      <td class="r">False</td>
	      <td class="de">View of call records. The view value specified for 'FSync' will also be applied for 'ISync' by default, since it cannot be changed for ISync</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listExtensionActiveCalls" aria-expanded="true" aria-controls="listExtensionActiveCalls">Get User Active Calls</a> 
        
      </td>
      <td class="description"><p>Returns records of all extension calls that are in progress, ordered by start time in descending order.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/active-calls <a href="https://developers.ringcentral.com/api-reference/Call-Log/listExtensionActiveCalls" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listExtensionActiveCalls" class="collapse" aria-labelledby="listExtensionActiveCalls">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">direction</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The direction for the result records. If not specified, both inbound and outbound records are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are allowed</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Call type of a record. If not specified, all call types are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">view</td>
	      <td class="t">string</td>
	      <td class="d">Simple</td>
	      <td class="r">False</td>
	      <td class="de">View of call records. The same view parameter specified for FSync will be applied for ISync, the view cannot be changed for ISync</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readCompanyCallLog" aria-expanded="true" aria-controls="readCompanyCallLog">Get Company Call Log Records</a> 
        
      </td>
      <td class="description"><p>Returns call log records filtered by parameters specified.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-log <a href="https://developers.ringcentral.com/api-reference/Call-Log/readCompanyCallLog" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCompanyCallLog" class="collapse" aria-labelledby="readCompanyCallLog">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">dateFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The start datetime for resulting records in (ISO 8601)[https://en.wikipedia.org/wiki/ISO_8601]  format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is dateTo minus 24 hours</td>
            </tr>
<tr>
	      <td class="n">dateTo</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The end datetime for resulting records in (ISO 8601)[https://en.wikipedia.org/wiki/ISO_8601]  format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is current time</td>
            </tr>
<tr>
	      <td class="n">direction</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The direction for the result records. If not specified, both inbound and outbound records are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">extensionNumber</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Extension number of a user. If specified, returns call log for a particular extension only</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">phoneNumber</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Phone number of a caller/call recipient. If specified, returns all calls (both incoming and outcoming) with the phone number specified. Cannot be specified together with the extensionNumber filter</td>
            </tr>
<tr>
	      <td class="n">recordingType</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Type of a call recording. If not specified, then calls without recordings are also returned</td>
            </tr>
<tr>
	      <td class="n">sessionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a call session</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Call type of a record. If not specified, all call types are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">view</td>
	      <td class="t">string</td>
	      <td class="d">Simple</td>
	      <td class="r">False</td>
	      <td class="de">View of call records. The same view parameter specified for FSync will be applied for ISync, the view cannot be changed for ISync</td>
            </tr>
<tr>
	      <td class="n">withRecording</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">**Deprecated**. Supported for compatibility reasons only. `true` if only recorded calls are returned. The default value is `false`. If both `withRecording` and `recordingType` are specified, `withRecording` is ignored</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#syncAccountCallLog" aria-expanded="true" aria-controls="syncAccountCallLog">Sync Company Call Log</a> 
        
      </td>
      <td class="description"><p>Synchronizes company call log records.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-log-sync <a href="https://developers.ringcentral.com/api-reference/Call-Log/syncAccountCallLog" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="syncAccountCallLog" class="collapse" aria-labelledby="syncAccountCallLog">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">dateFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The start datetime for resulting records in (ISO 8601)[https://en.wikipedia.org/wiki/ISO_8601]  format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is the current moment</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">For 'FSync' the parameter is mandatory, it limits the number of records to be returned in response. For 'ISync' it specifies with how many records to extend sync frame to the past, the maximum number of records is 250</td>
            </tr>
<tr>
	      <td class="n">showDeleted</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">False</td>
	      <td class="de">Supported for ISync. If 'True' then deleted call records are returned</td>
            </tr>
<tr>
	      <td class="n">statusGroup</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of calls to be returned.</td>
            </tr>
<tr>
	      <td class="n">syncToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Value of syncToken property of last sync request response</td>
            </tr>
<tr>
	      <td class="n">syncType</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of synchronization. 'FSync' is a default value</td>
            </tr>
<tr>
	      <td class="n">view</td>
	      <td class="t">string</td>
	      <td class="d">Simple</td>
	      <td class="r">False</td>
	      <td class="de">View of call records. The same view parameter specified for FSync will be applied for ISync, the view cannot be changed for ISync</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readCompanyCallRecord" aria-expanded="true" aria-controls="readCompanyCallRecord">Get Company Call Log Record(s)</a> 
        
      </td>
      <td class="description"><p>Returns individual call log record(s) by ID(s). Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-log/{callRecordId} <a href="https://developers.ringcentral.com/api-reference/Call-Log/readCompanyCallRecord" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCompanyCallRecord" class="collapse" aria-labelledby="readCompanyCallRecord">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">callRecordId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call log record</td>
            </tr>
<tr>
	      <td class="n">view</td>
	      <td class="t">string</td>
	      <td class="d">Simple</td>
	      <td class="r">False</td>
	      <td class="de">View of call records. The view value specified for 'FSync' will also be applied for 'ISync' by default, since it cannot be changed for ISync</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listCompanyActiveCalls" aria-expanded="true" aria-controls="listCompanyActiveCalls">Get Company Active Calls</a> 
        
      </td>
      <td class="description"><p>Returns records of all calls that are in progress, ordered by start time in descending order.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/active-calls <a href="https://developers.ringcentral.com/api-reference/Call-Log/listCompanyActiveCalls" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCompanyActiveCalls" class="collapse" aria-labelledby="listCompanyActiveCalls">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">direction</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The direction for the result records. If not specified, both inbound and outbound records are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">transport</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Call transport type. 'PSTN' specifies that a call leg is initiated from the PSTN network provider; 'VoIP' - from an RC phone. By default this filter is disabled</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Call type of a record. If not specified, all call types are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">view</td>
	      <td class="t">string</td>
	      <td class="d">Simple</td>
	      <td class="r">False</td>
	      <td class="de">View of call records. The same view parameter specified for FSync will be applied for ISync, the view cannot be changed for ISync</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Call Monitoring Groups

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createCallMonitoringGroup" aria-expanded="true" aria-controls="createCallMonitoringGroup">Create Call Monitoring Group</a> 
        
      </td>
      <td class="description"><p>Creates a new call monitoring group.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/call-monitoring-groups <a href="https://developers.ringcentral.com/api-reference/Call-Monitoring-Groups/createCallMonitoringGroup" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createCallMonitoringGroup" class="collapse" aria-labelledby="createCallMonitoringGroup">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Parameters of a call monitoring group that will be created</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listCallMonitoringGroups" aria-expanded="true" aria-controls="listCallMonitoringGroups">Get Call Monitoring Groups List</a> 
        
      </td>
      <td class="description"><p>Returns call monitoring groups that can be filtered by some extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-monitoring-groups <a href="https://developers.ringcentral.com/api-reference/Call-Monitoring-Groups/listCallMonitoringGroups" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCallMonitoringGroups" class="collapse" aria-labelledby="listCallMonitoringGroups">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">memberExtensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Internal identifier of an extension that is a member of every group within the result</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are allowed</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateCallMonitoringGroup" aria-expanded="true" aria-controls="updateCallMonitoringGroup">Updates Call Monitoring Group</a> 
        
      </td>
      <td class="description"><p>Updates call monitoring group name by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/call-monitoring-groups/{groupId} <a href="https://developers.ringcentral.com/api-reference/Call-Monitoring-Groups/updateCallMonitoringGroup" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateCallMonitoringGroup" class="collapse" aria-labelledby="updateCallMonitoringGroup">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Parameters of a call monitoring group that will be updated</td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a call monitoring group</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteCallMonitoringGroup" aria-expanded="true" aria-controls="deleteCallMonitoringGroup">Delete Call Monitoring Group</a> 
        
      </td>
      <td class="description"><p>Remove infromation about the given call monitoring group.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/call-monitoring-groups/{groupId} <a href="https://developers.ringcentral.com/api-reference/Call-Monitoring-Groups/deleteCallMonitoringGroup" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteCallMonitoringGroup" class="collapse" aria-labelledby="deleteCallMonitoringGroup">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listCallMonitoringGroupMembers" aria-expanded="true" aria-controls="listCallMonitoringGroupMembers">Get Call Monitoring Group Member List</a> 
        
      </td>
      <td class="description"><p>Returns call monitoring group members.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-monitoring-groups/{groupId}/members <a href="https://developers.ringcentral.com/api-reference/Call-Monitoring-Groups/listCallMonitoringGroupMembers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCallMonitoringGroupMembers" class="collapse" aria-labelledby="listCallMonitoringGroupMembers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are allowed</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateCallMonitoringGroupList" aria-expanded="true" aria-controls="updateCallMonitoringGroupList">Update Call Monitoring Group List</a> 
        
      </td>
      <td class="description"><p>Updates call monitoring groups.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/call-monitoring-groups/{groupId}/bulk-assign <a href="https://developers.ringcentral.com/api-reference/Call-Monitoring-Groups/updateCallMonitoringGroupList" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateCallMonitoringGroupList" class="collapse" aria-labelledby="updateCallMonitoringGroupList">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Changes for the given group</td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Call Queues

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listCallQueues" aria-expanded="true" aria-controls="listCallQueues">Get Call Queue List</a> 
        
      </td>
      <td class="description"><p>Returns call queue group list.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-queues <a href="https://developers.ringcentral.com/api-reference/Call-Queues/listCallQueues" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCallQueues" class="collapse" aria-labelledby="listCallQueues">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">memberExtensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Internal identifier of an extension that is a member of every group within the result</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listCallQueueMembers" aria-expanded="true" aria-controls="listCallQueueMembers">Get Call Queue Members</a> 
        
      </td>
      <td class="description"><p>Returns call queue group members.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-queues/{groupId}/members <a href="https://developers.ringcentral.com/api-reference/Call-Queues/listCallQueueMembers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCallQueueMembers" class="collapse" aria-labelledby="listCallQueueMembers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are allowed</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#assignMultipleCallQueueMembers" aria-expanded="true" aria-controls="assignMultipleCallQueueMembers">Assign Multiple Call Queue Members</a> 
        
      </td>
      <td class="description"><p>Updates a call queue group.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/call-queues/{groupId}/bulk-assign <a href="https://developers.ringcentral.com/api-reference/Call-Queues/assignMultipleCallQueueMembers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="assignMultipleCallQueueMembers" class="collapse" aria-labelledby="assignMultipleCallQueueMembers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Changes for the given group</td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateUserCallQueues" aria-expanded="true" aria-controls="updateUserCallQueues">Update User Call Queues</a> 
        
      </td>
      <td class="description"><p>Updates the list of call queues where the user is an agent. This is a full update request, which means that if any queue where the user is an agent is not mentioned in request, then the user is automatically removed from this queue.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/call-queues <a href="https://developers.ringcentral.com/api-reference/Call-Queues/updateUserCallQueues" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateUserCallQueues" class="collapse" aria-labelledby="updateUserCallQueues">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listDepartmentMembers" aria-expanded="true" aria-controls="listDepartmentMembers">Get Department Member List</a> 
        
      </td>
      <td class="description"><p>Viewing user account info (including name, business name, address and phone number/account number)</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/department/{departmentId}/members <a href="https://developers.ringcentral.com/api-reference/Call-Queues/listDepartmentMembers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listDepartmentMembers" class="collapse" aria-labelledby="listDepartmentMembers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">departmentId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a Department extension (same as extensionId but only the ID of a department extension is valid)</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#assignMultipleDepartmentMembers" aria-expanded="true" aria-controls="assignMultipleDepartmentMembers">Assign Multiple Department Members</a> 
        
      </td>
      <td class="description"><p>Adds and/or removes multiple call queue members</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/department/bulk-assign <a href="https://developers.ringcentral.com/api-reference/Call-Queues/assignMultipleDepartmentMembers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="assignMultipleDepartmentMembers" class="collapse" aria-labelledby="assignMultipleDepartmentMembers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Call Recordings

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readCallRecording" aria-expanded="true" aria-controls="readCallRecording">Get Call Recording</a> 
        
      </td>
      <td class="description"><p>Returns call recordings by ID(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/recording/{recordingId} <a href="https://developers.ringcentral.com/api-reference/Call-Recordings/readCallRecording" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCallRecording" class="collapse" aria-labelledby="readCallRecording">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">recordingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a recording (returned in Call Log)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listCallRecordingData" aria-expanded="true" aria-controls="listCallRecordingData">Get Call Recordings Data</a> 
        
      </td>
      <td class="description"><p>Returns media content of a call recording.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/recording/{recordingId}/content <a href="https://developers.ringcentral.com/api-reference/Call-Recordings/listCallRecordingData" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCallRecordingData" class="collapse" aria-labelledby="listCallRecordingData">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">recordingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a recording (returned in Call Log)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Call Routing

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createIVRPrompt" aria-expanded="true" aria-controls="createIVRPrompt">Create IVR Prompts</a> 
        
      </td>
      <td class="description"><p>Creates an IVR prompt.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/ivr-prompts <a href="https://developers.ringcentral.com/api-reference/Call-Routing/createIVRPrompt" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createIVRPrompt" class="collapse" aria-labelledby="createIVRPrompt">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">attachment</td>
	      <td class="t">file</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Audio file that will be used as a prompt. Attachment cannot be empty, only audio files are supported</td>
            </tr>
<tr>
	      <td class="n">name</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Description of file contents.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get IVR Prompt List 
	
      </td>
      <td class="description"><p>Returns the list of IVR prompts.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/ivr-prompts <a href="https://developers.ringcentral.com/api-reference/Call-Routing/listIVRPrompts" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listIVRPrompts" class="collapse" aria-labelledby="listIVRPrompts">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readIVRPrompt" aria-expanded="true" aria-controls="readIVRPrompt">Get IVR Prompt</a> 
        
      </td>
      <td class="description"><p>Returns an IVR prompt by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/ivr-prompts/{promptId} <a href="https://developers.ringcentral.com/api-reference/Call-Routing/readIVRPrompt" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readIVRPrompt" class="collapse" aria-labelledby="readIVRPrompt">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">promptId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteIVRPrompt" aria-expanded="true" aria-controls="deleteIVRPrompt">Delete IVR Prompt</a> 
        
      </td>
      <td class="description"><p>Deletes an IVR prompt by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/ivr-prompts/{promptId} <a href="https://developers.ringcentral.com/api-reference/Call-Routing/deleteIVRPrompt" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteIVRPrompt" class="collapse" aria-labelledby="deleteIVRPrompt">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">promptId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateIVRPrompt" aria-expanded="true" aria-controls="updateIVRPrompt">Update IVR Prompt</a> 
        
      </td>
      <td class="description"><p>Updates an IVR prompt by ID</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/ivr-prompts/{promptId} <a href="https://developers.ringcentral.com/api-reference/Call-Routing/updateIVRPrompt" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateIVRPrompt" class="collapse" aria-labelledby="updateIVRPrompt">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">promptId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readIVRPromptContent" aria-expanded="true" aria-controls="readIVRPromptContent">Get IVR Prompt Content</a> 
        
      </td>
      <td class="description"><p>Returns media content of an IVR prompt by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/ivr-prompts/{promptId}/content <a href="https://developers.ringcentral.com/api-reference/Call-Routing/readIVRPromptContent" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readIVRPromptContent" class="collapse" aria-labelledby="readIVRPromptContent">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">promptId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createIVRMenu" aria-expanded="true" aria-controls="createIVRMenu">Create IVR Menu</a> 
        
      </td>
      <td class="description"><p>Creates a company IVR menu.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/ivr-menus <a href="https://developers.ringcentral.com/api-reference/Call-Routing/createIVRMenu" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createIVRMenu" class="collapse" aria-labelledby="createIVRMenu">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readIVRMenu" aria-expanded="true" aria-controls="readIVRMenu">Get IVR Menu</a> 
        
      </td>
      <td class="description"><p>Returns a company IVR menu by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/ivr-menus/{ivrMenuId} <a href="https://developers.ringcentral.com/api-reference/Call-Routing/readIVRMenu" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readIVRMenu" class="collapse" aria-labelledby="readIVRMenu">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">ivrMenuId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateIVRMenu" aria-expanded="true" aria-controls="updateIVRMenu">Update IVR Menu</a> 
        
      </td>
      <td class="description"><p>Updates a company IVR menu by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/ivr-menus/{ivrMenuId} <a href="https://developers.ringcentral.com/api-reference/Call-Routing/updateIVRMenu" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateIVRMenu" class="collapse" aria-labelledby="updateIVRMenu">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">ivrMenuId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Chats

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listGlipChats" aria-expanded="true" aria-controls="listGlipChats">Get Chats</a> 
        
      </td>
      <td class="description"><p>Returns the list of chats where the user is a member and also public teams that can be joined. All records in response are sorted by creation time of a chat in ascending order.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/chats <a href="https://developers.ringcentral.com/api-reference/Chats/listGlipChats" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listGlipChats" class="collapse" aria-labelledby="listGlipChats">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Pagination token.</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Number of chats to be fetched by one request. The maximum value is 250, by default - 30.</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of chats to be fetched. By default all type of chats will be fetched</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Chat 
	
      </td>
      <td class="description"><p>Returns information about a chat by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/chats/{chatId} <a href="https://developers.ringcentral.com/api-reference/Chats/readGlipChat" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipChat" class="collapse" aria-labelledby="readGlipChat">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listRecentChats" aria-expanded="true" aria-controls="listRecentChats">Get Recent Chats</a> 
        
      </td>
      <td class="description"><p>Returns recent chats where the user is a member. All records in response are sorted by the <code>lastModifiedTime</code> in descending order (the latest changed chat is displayed first on page)</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/recent/chats <a href="https://developers.ringcentral.com/api-reference/Chats/listRecentChats" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listRecentChats" class="collapse" aria-labelledby="listRecentChats">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Max number of chats to be fetched by one request (Not more than 250).</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of chats to be fetched. By default all chat types are returned</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Favorite Chats 
	
      </td>
      <td class="description"><p>Returns a list of the current user's favorite chats.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/favorites <a href="https://developers.ringcentral.com/api-reference/Chats/listFavoriteChats" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listFavoriteChats" class="collapse" aria-labelledby="listFavoriteChats">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Add Chat to Favorites 
	
      </td>
      <td class="description"><p>Adds the specified chat to the users's list of favorites.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/chats/{chatId}/favorite <a href="https://developers.ringcentral.com/api-reference/Chats/favoriteGlipChat" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="favoriteGlipChat" class="collapse" aria-labelledby="favoriteGlipChat">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Remove Chat from Favorites 
	
      </td>
      <td class="description"><p>Removes the specified chat from the users's list of favorites.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/chats/{chatId}/unfavorite <a href="https://developers.ringcentral.com/api-reference/Chats/unfavoriteGlipChat" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="unfavoriteGlipChat" class="collapse" aria-labelledby="unfavoriteGlipChat">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Mark Chat as Read 
	
      </td>
      <td class="description"><p>Sets the specified chat status to 'Read' for the current user.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/chats/{chatId}/read <a href="https://developers.ringcentral.com/api-reference/Chats/markChatRead" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="markChatRead" class="collapse" aria-labelledby="markChatRead">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Mark Chat as Unread 
	
      </td>
      <td class="description"><p>Sets the specified chat status to 'Unread' for the current user.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/chats/{chatId}/unread <a href="https://developers.ringcentral.com/api-reference/Chats/markChatUnread" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="markChatUnread" class="collapse" aria-labelledby="markChatUnread">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listGlipGroups" aria-expanded="true" aria-controls="listGlipGroups">Get User Groups</a> 
        
      </td>
      <td class="description"><p>Returns the list of groups where the user is a member.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/groups <a href="https://developers.ringcentral.com/api-reference/Chats/listGlipGroups" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listGlipGroups" class="collapse" aria-labelledby="listGlipGroups">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Pagination token.</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Number of groups to be fetched by one request. The maximum value is 250, by default - 30</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of groups to be fetched (by default all type of groups will be fetched)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Create Group 
	
      </td>
      <td class="description"><p>Creates a new private chat/team.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/groups <a href="https://developers.ringcentral.com/api-reference/Chats/createGlipGroup" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createGlipGroup" class="collapse" aria-labelledby="createGlipGroup">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Group 
	
      </td>
      <td class="description"><p>Returns information about a group or multiple groups by their ID(s). Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/groups/{groupId} <a href="https://developers.ringcentral.com/api-reference/Chats/readGlipGroup" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipGroup" class="collapse" aria-labelledby="readGlipGroup">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#assignGlipGroupMembers" aria-expanded="true" aria-controls="assignGlipGroupMembers">Edit Group Members</a> 
        
      </td>
      <td class="description"><p>Updates group members. <strong>Please note:</strong> Only groups of 'Team' type can be updated. Currently only one operation at a time (either adding or removal) is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/groups/{groupId}/bulk-assign <a href="https://developers.ringcentral.com/api-reference/Chats/assignGlipGroupMembers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="assignGlipGroupMembers" class="collapse" aria-labelledby="assignGlipGroupMembers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a group</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Company

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        Get Account Info 
	
      </td>
      <td class="description"><p>Returns basic information about a particular RingCentral customer account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId} <a href="https://developers.ringcentral.com/api-reference/Company/readAccountInfo" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAccountInfo" class="collapse" aria-labelledby="readAccountInfo">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Account Business Address 
	
      </td>
      <td class="description"><p>Returns business address of a company.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/business-address <a href="https://developers.ringcentral.com/api-reference/Company/readAccountBusinessAddress" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAccountBusinessAddress" class="collapse" aria-labelledby="readAccountBusinessAddress">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateAccountBusinessAddress" aria-expanded="true" aria-controls="updateAccountBusinessAddress">Update Company Business Address</a> 
        
      </td>
      <td class="description"><p>Updates the business address of a company that account is linked to. Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/business-address <a href="https://developers.ringcentral.com/api-reference/Company/updateAccountBusinessAddress" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateAccountBusinessAddress" class="collapse" aria-labelledby="updateAccountBusinessAddress">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Account Service Info 
	
      </td>
      <td class="description"><p>Returns the information about service plan, available features and limitations for a particular RingCentral customer account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/service-info <a href="https://developers.ringcentral.com/api-reference/Company/readAccountServiceInfo" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAccountServiceInfo" class="collapse" aria-labelledby="readAccountServiceInfo">
</div>
      </td>
    </tr>
</tbody>
</table>

### Conversations

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listGlipConversations" aria-expanded="true" aria-controls="listGlipConversations">Get Conversations</a> 
        
      </td>
      <td class="description"><p>Returns the list of conversations where the user is a member. All records in response are sorted by creation time of a chat in ascending order.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/conversations <a href="https://developers.ringcentral.com/api-reference/Conversations/listGlipConversations" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listGlipConversations" class="collapse" aria-labelledby="listGlipConversations">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Pagination token.</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Number of conversations to be fetched by one request. The maximum value is 250, by default - 30</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Create/Open Conversation 
	
      </td>
      <td class="description"><p>Creates a new conversation or opens the existing one. If the conversation already exists, then its ID will be returned in response. A conversation is an adhoc discussion between a particular set of users, not featuring any specific name or description. If you add a person to the existing conversation, it creates a whole new conversation.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/conversations <a href="https://developers.ringcentral.com/api-reference/Conversations/createGlipConversation" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createGlipConversation" class="collapse" aria-labelledby="createGlipConversation">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Conversation 
	
      </td>
      <td class="description"><p>Returns information about the specified conversation, including the list of conversation participants. A conversation is an adhoc discussion between a particular set of users, not featuring any specific name or description. If you add a person to the existing conversation, it creates a whole new conversation.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/conversations/{chatId} <a href="https://developers.ringcentral.com/api-reference/Conversations/readGlipConversation" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipConversation" class="collapse" aria-labelledby="readGlipConversation">
</div>
      </td>
    </tr>
</tbody>
</table>

### Custom Fields

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createCustomField" aria-expanded="true" aria-controls="createCustomField">Create Custom Field</a> 
        
      </td>
      <td class="description"><p>Creates custom field attached to the object.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/custom-fields <a href="https://developers.ringcentral.com/api-reference/Custom-Fields/createCustomField" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createCustomField" class="collapse" aria-labelledby="createCustomField">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Custom Field List 
	
      </td>
      <td class="description"><p>Returns the list of created custom fields.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/custom-fields <a href="https://developers.ringcentral.com/api-reference/Custom-Fields/listCustomFields" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCustomFields" class="collapse" aria-labelledby="listCustomFields">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateCustomField" aria-expanded="true" aria-controls="updateCustomField">Update Сustom Field</a> 
        
      </td>
      <td class="description"><p>Updates custom field by ID specified in path.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/custom-fields/{fieldId} <a href="https://developers.ringcentral.com/api-reference/Custom-Fields/updateCustomField" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateCustomField" class="collapse" aria-labelledby="updateCustomField">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">fieldId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Custom field identifier</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteCustomField" aria-expanded="true" aria-controls="deleteCustomField">Delete Custom Field</a> 
        
      </td>
      <td class="description"><p>Deletes custom field(s) by ID(s) with the corresponding values.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/custom-fields/{fieldId} <a href="https://developers.ringcentral.com/api-reference/Custom-Fields/deleteCustomField" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteCustomField" class="collapse" aria-labelledby="deleteCustomField">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">fieldId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Custom field identifier</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Devices

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readDevice" aria-expanded="true" aria-controls="readDevice">Get Device</a> 
        
      </td>
      <td class="description"><p>Returns account device(s) by their ID(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/device/{deviceId} <a href="https://developers.ringcentral.com/api-reference/Devices/readDevice" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readDevice" class="collapse" aria-labelledby="readDevice">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">deviceId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a device</td>
            </tr>
<tr>
	      <td class="n">syncEmergencyAddress</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">false</td>
	      <td class="de">Specifies if emergency address should be synchronized or not</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateDevice" aria-expanded="true" aria-controls="updateDevice">Update Device</a> 
        
      </td>
      <td class="description"><p>Updates account device(s) by their ID(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/device/{deviceId} <a href="https://developers.ringcentral.com/api-reference/Devices/updateDevice" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateDevice" class="collapse" aria-labelledby="updateDevice">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">deviceId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">prestatement</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listExtensionDevices" aria-expanded="true" aria-controls="listExtensionDevices">Get Extension Device List</a> 
        
      </td>
      <td class="description"><p>Returns devices of the extension(s) by their ID(s). Batch request is supported</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/device <a href="https://developers.ringcentral.com/api-reference/Devices/listExtensionDevices" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listExtensionDevices" class="collapse" aria-labelledby="listExtensionDevices">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">feature</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Device feature or multiple features supported</td>
            </tr>
<tr>
	      <td class="n">linePooling</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Pooling type of a device</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Extensions

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listExtensions" aria-expanded="true" aria-controls="listExtensions">Get Extension List</a> 
        
      </td>
      <td class="description"><p>Returns the list of extensions created for a particular account. All types of extensions are included in this list.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension <a href="https://developers.ringcentral.com/api-reference/Extensions/listExtensions" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listExtensions" class="collapse" aria-labelledby="listExtensions">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">email</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Extension email address</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Extension number to retrieve</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are allowed</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">status</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Extension current state. Multiple values are supported. If 'Unassigned' is specified, then extensions without `extensionNumber` attribute are returned. If not specified, then all extensions are returned.</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Extension type. Multiple values are supported</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createExtension" aria-expanded="true" aria-controls="createExtension">Create Extension</a> 
        
      </td>
      <td class="description"><p>Creates an extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension <a href="https://developers.ringcentral.com/api-reference/Extensions/createExtension" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createExtension" class="collapse" aria-labelledby="createExtension">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listUserTemplates" aria-expanded="true" aria-controls="listUserTemplates">Get User Template List</a> 
        
      </td>
      <td class="description"><p>Returns the list of user templates for the current account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/templates <a href="https://developers.ringcentral.com/api-reference/Extensions/listUserTemplates" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listUserTemplates" class="collapse" aria-labelledby="listUserTemplates">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readUserTemplate" aria-expanded="true" aria-controls="readUserTemplate">Get User Template</a> 
        
      </td>
      <td class="description"><p>Returns the user template by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/templates/{templateId} <a href="https://developers.ringcentral.com/api-reference/Extensions/readUserTemplate" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUserTemplate" class="collapse" aria-labelledby="readUserTemplate">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">templateId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### External Contacts

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listContacts" aria-expanded="true" aria-controls="listContacts">Get Contact List</a> 
        
      </td>
      <td class="description"><p>Returns user personal contacts.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact <a href="https://developers.ringcentral.com/api-reference/External-Contacts/listContacts" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listContacts" class="collapse" aria-labelledby="listContacts">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">phoneNumber</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">sortBy</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Sorts results by the specified property</td>
            </tr>
<tr>
	      <td class="n">startsWith</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">If specified, only contacts whose First name or Last name start with the mentioned substring are returned. Case-insensitive</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createContact" aria-expanded="true" aria-controls="createContact">Create Contact</a> 
        
      </td>
      <td class="description"><p>Creates personal user contact.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact <a href="https://developers.ringcentral.com/api-reference/External-Contacts/createContact" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createContact" class="collapse" aria-labelledby="createContact">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">dialingPlan</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">A country code value complying with the [ISO 3166-1 alpha-2](https://ru.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. The default value is home country of the current extension</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readContact" aria-expanded="true" aria-controls="readContact">Get Contact</a> 
        
      </td>
      <td class="description"><p>Returns contact(s) by ID(s). Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact/{contactId} <a href="https://developers.ringcentral.com/api-reference/External-Contacts/readContact" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readContact" class="collapse" aria-labelledby="readContact">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">contactId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a contact record in the RingCentral database</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateContact" aria-expanded="true" aria-controls="updateContact">Update Contact</a> 
        
      </td>
      <td class="description"><p>Updates personal contact information by contact ID(s). Batch request is supported</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact/{contactId} <a href="https://developers.ringcentral.com/api-reference/External-Contacts/updateContact" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateContact" class="collapse" aria-labelledby="updateContact">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">contactId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a contact record in the RingCentral database</td>
            </tr>
<tr>
	      <td class="n">dialingPlan</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">A country code value complying with the [ISO 3166-1 alpha-2](https://ru.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. The default value is home country of the current extension</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteContact" aria-expanded="true" aria-controls="deleteContact">Delete Contact</a> 
        
      </td>
      <td class="description"><p>Deletes contact(s) by ID(s). Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact/{contactId} <a href="https://developers.ringcentral.com/api-reference/External-Contacts/deleteContact" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteContact" class="collapse" aria-labelledby="deleteContact">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">contactId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a contact record in the RingCentral database</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#syncAddressBook" aria-expanded="true" aria-controls="syncAddressBook">Address Book Synchronization</a> 
        
      </td>
      <td class="description"><p>Synchronizes user contacts.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book-sync <a href="https://developers.ringcentral.com/api-reference/External-Contacts/syncAddressBook" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="syncAddressBook" class="collapse" aria-labelledby="syncAddressBook">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">pageId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a page. It can be obtained from the 'nextPageId' parameter passed in response body</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Number of records per page to be returned. The max number of records is 250, which is also the default. For 'FSync' if the number of records exceeds the parameter value (either specified or default), all of the pages can be retrieved in several requests. For 'ISync' if the number of records exceeds the page size, the number of incoming changes to this number is limited</td>
            </tr>
<tr>
	      <td class="n">syncToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Value of syncToken property of the last sync request response</td>
            </tr>
<tr>
	      <td class="n">syncType</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of synchronization</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listFavoriteContacts" aria-expanded="true" aria-controls="listFavoriteContacts">Get Favorite Contact List</a> 
        
      </td>
      <td class="description"><p>Returns the list of favorite contacts of the current extension. Favorite contacts include both company contacts (extensions) and personal contacts (address book records).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/favorite <a href="https://developers.ringcentral.com/api-reference/External-Contacts/listFavoriteContacts" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listFavoriteContacts" class="collapse" aria-labelledby="listFavoriteContacts">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateFavoriteContactList" aria-expanded="true" aria-controls="updateFavoriteContactList">Update Favorite Contact List</a> 
        
      </td>
      <td class="description"><p>Updates the list of favorite contacts of the current extension. Favorite contacts include both company contacts (extensions) and personal contacts (address book records).<strong>Please note</strong>: currently personal address book size is limited to 10 000 contacts.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/favorite <a href="https://developers.ringcentral.com/api-reference/External-Contacts/updateFavoriteContactList" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateFavoriteContactList" class="collapse" aria-labelledby="updateFavoriteContactList">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Fax

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createFaxMessage" aria-expanded="true" aria-controls="createFaxMessage">Create Fax Message</a> 
        
      </td>
      <td class="description"><p>Creates and sends/resends a fax message. Resend can be implemented if sending has failed. Fax attachment size (both single and total) is limited to 50Mb.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/fax <a href="https://developers.ringcentral.com/api-reference/Fax/createFaxMessage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createFaxMessage" class="collapse" aria-labelledby="createFaxMessage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account (integer) or tilde (~) to indicate the account which was logged-in within the current session.</td>
            </tr>
<tr>
	      <td class="n">attachment</td>
	      <td class="t">file</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">File to upload</td>
            </tr>
<tr>
	      <td class="n">coverIndex</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Cover page identifier. For the list of available cover page identifiers please call the method Fax Cover Pages. If not specified, the default cover page which is configured in 'Outbound Fax Settings' is attached</td>
            </tr>
<tr>
	      <td class="n">coverPageText</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Cover page text, entered by the fax sender and printed on the cover page. Maximum length is limited to 1024 symbols</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension (integer) or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">faxResolution</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Resolution of Fax</td>
            </tr>
<tr>
	      <td class="n">isoCode</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">ISO Code. e.g UK</td>
            </tr>
<tr>
	      <td class="n">sendTime</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Timestamp to send fax at. If not specified (current or the past), the fax is sent immediately</td>
            </tr>
<tr>
	      <td class="n">to</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">To Phone Number</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listFaxCoverPages" aria-expanded="true" aria-controls="listFaxCoverPages">Get Fax Cover Page List</a> 
        
      </td>
      <td class="description"><p>Returns fax cover pages available for the current extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/fax-cover-page <a href="https://developers.ringcentral.com/api-reference/Fax/listFaxCoverPages" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listFaxCoverPages" class="collapse" aria-labelledby="listFaxCoverPages">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Features

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readUserFeatures" aria-expanded="true" aria-controls="readUserFeatures">Get User Features</a> 
        
      </td>
      <td class="description"><p>Returns the list of supported features and information on their availability for the current extension. Specific feature(s) might be checked by providing <code>featureId</code> query param. Multiple values supported, format: <code>?featureId=Feature1&amp;featureId=Feature2</code>. To get only available features in order to decrease response size, <code>availableOnly=true</code> query param might be specified.
In case the feature is available for the current user, <code>"available": true</code> is returned in the response for the record with corresponding feature <code>id</code>. Otherwise, additional attribute <code>reason</code> is returned with the appropriate code:
* <code>ServicePlanLimitation</code> - the feature not included to the account service plan;
* <code>AccountLimitation</code> - the feature is turned off for the account;
* <code>ExtensionTypeLimitation</code> - the feature is not applicable for the extension type;
* <code>ExtensionLimitation</code> - the feature is not available for the extension, e.g., additional license required;
* <code>InsufficientPermissions</code> - required permission not granted to the current user (not the one, who is specified in the URL, but the one who's access token is used);
* <code>ConfigurationLimitation</code> - the feature is turned off for the extension, e.g., by the account administrator.</p>
<p>Also, some feature may have some additional parameters, e.g., limits, which are returned in <code>params</code> attribute as a name-value collection:</p>
<pre><code>{
  "id": "HUD",
  "available": true,
  "params": [
    {
      "name": "limitMax",
      "value": "100"
    }
  ]
}
</code></pre></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/features <a href="https://developers.ringcentral.com/api-reference/Features/readUserFeatures" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUserFeatures" class="collapse" aria-labelledby="readUserFeatures">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">availableOnly</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">featureId</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Glip Compliance Exports

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        Create Data Export Task 
	
      </td>
      <td class="description"><p>Creates a task for Glip data export and returns a link at which the exported data will be available in future once the task is implemented. The exported data can be downloaded by calling Get Data Export Task method with the specified task ID. Simultaneously no more than 2 tasks per company can be created.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/data-export <a href="https://developers.ringcentral.com/api-reference/Glip-Compliance-Exports/createDataExportTask" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createDataExportTask" class="collapse" aria-labelledby="createDataExportTask">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listDataExportTasks" aria-expanded="true" aria-controls="listDataExportTasks">Get Data Export Task List</a> 
        
      </td>
      <td class="description"><p>Returns the list of Glip data export tasks.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/data-export <a href="https://developers.ringcentral.com/api-reference/Glip-Compliance-Exports/listDataExportTasks" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listDataExportTasks" class="collapse" aria-labelledby="listDataExportTasks">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">false</td>
	      <td class="de">Page number to be retrieved; value range is > 0</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">false</td>
	      <td class="de">Number of records to be returned per page; value range is 1 - 250</td>
            </tr>
<tr>
	      <td class="n">status</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Status of the task(s) to be returned. Multiple values are supported</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Data Export Task 
	
      </td>
      <td class="description"><p>Returns the links for downloading Glip data exported within the specified task. If the export task is still in progress, then only the task status will be returned. If the data is ready for downloading, then the list of URLs will be returned.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/data-export/{taskId} <a href="https://developers.ringcentral.com/api-reference/Glip-Compliance-Exports/readDataExportTask" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readDataExportTask" class="collapse" aria-labelledby="readDataExportTask">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readDataExportTaskDataset" aria-expanded="true" aria-controls="readDataExportTaskDataset">Get Data Export Task Dataset</a> 
        
      </td>
      <td class="description"><p>Returns the specified dataset by ID. Each dataset is a ZIP archive the size of which is limited to 1 Gb.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/data-export/{taskId}/datasets/{datasetId} <a href="https://developers.ringcentral.com/api-reference/Glip-Compliance-Exports/readDataExportTaskDataset" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readDataExportTaskDataset" class="collapse" aria-labelledby="readDataExportTaskDataset">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">datasetId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a dataset</td>
            </tr>
<tr>
	      <td class="n">taskId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a task</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Glip Profile

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        Get Person 
	
      </td>
      <td class="description"><p>Returns a user or multiple users by their ID(s). Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/persons/{personId} <a href="https://developers.ringcentral.com/api-reference/Glip-Profile/readGlipPerson" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipPerson" class="collapse" aria-labelledby="readGlipPerson">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Company Info 
	
      </td>
      <td class="description"><p>Returns information about one or more companies by their IDs.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/companies/{companyId} <a href="https://developers.ringcentral.com/api-reference/Glip-Profile/readGlipCompany" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipCompany" class="collapse" aria-labelledby="readGlipCompany">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Preferences 
	
      </td>
      <td class="description"><p>Returns information about user preferences.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/preferences <a href="https://developers.ringcentral.com/api-reference/Glip-Profile/readGlipPreferences" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipPreferences" class="collapse" aria-labelledby="readGlipPreferences">
</div>
      </td>
    </tr>
</tbody>
</table>

### Glip Webhooks

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        Create Webhook in Group 
	
      </td>
      <td class="description"><p>Creates a new webhook</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/groups/{groupId}/webhooks <a href="https://developers.ringcentral.com/api-reference/Glip-Webhooks/createGlipGroupWebhook" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createGlipGroupWebhook" class="collapse" aria-labelledby="createGlipGroupWebhook">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Webhooks in Group 
	
      </td>
      <td class="description"><p>Returns webhooks which are available for the current user by group ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/groups/{groupId}/webhooks <a href="https://developers.ringcentral.com/api-reference/Glip-Webhooks/listGlipGroupWebhooks" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listGlipGroupWebhooks" class="collapse" aria-labelledby="listGlipGroupWebhooks">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Webhooks 
	
      </td>
      <td class="description"><p>Returns a list of all webhooks associated with the current account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/webhooks <a href="https://developers.ringcentral.com/api-reference/Glip-Webhooks/listGlipWebhooks" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listGlipWebhooks" class="collapse" aria-labelledby="listGlipWebhooks">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Webhook 
	
      </td>
      <td class="description"><p>Returns webhooks(s) with the specified id(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/webhooks/{webhookId} <a href="https://developers.ringcentral.com/api-reference/Glip-Webhooks/readGlipWebhook" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipWebhook" class="collapse" aria-labelledby="readGlipWebhook">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Delete Webhook 
	
      </td>
      <td class="description"><p>Deletes the webhook by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/glip/webhooks/{webhookId} <a href="https://developers.ringcentral.com/api-reference/Glip-Webhooks/deleteGlipWebhook" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteGlipWebhook" class="collapse" aria-labelledby="deleteGlipWebhook">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Activate Webhook 
	
      </td>
      <td class="description"><p>Activates webhook by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/webhooks/{webhookId}/activate <a href="https://developers.ringcentral.com/api-reference/Glip-Webhooks/activateGlipWebhook" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="activateGlipWebhook" class="collapse" aria-labelledby="activateGlipWebhook">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Suspend Webhook 
	
      </td>
      <td class="description"><p>Suspends webhook by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/webhooks/{webhookId}/suspend <a href="https://developers.ringcentral.com/api-reference/Glip-Webhooks/suspendGlipWebhook" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="suspendGlipWebhook" class="collapse" aria-labelledby="suspendGlipWebhook">
</div>
      </td>
    </tr>
</tbody>
</table>

### Internal Contacts

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#searchDirectoryEntries" aria-expanded="true" aria-controls="searchDirectoryEntries">Search Company Directory Entries</a> 
        
      </td>
      <td class="description"><p>Returns contact information on corporate users of federated accounts according to the specified filtering and ordering.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/directory/entries/search <a href="https://developers.ringcentral.com/api-reference/Internal-Contacts/searchDirectoryEntries" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="searchDirectoryEntries" class="collapse" aria-labelledby="searchDirectoryEntries">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readDirectoryEntry" aria-expanded="true" aria-controls="readDirectoryEntry">Get Corporate Directory Entry</a> 
        
      </td>
      <td class="description"><p>Returns contact information on a particular corporate user of a federated account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/directory/entries/{entryId} <a href="https://developers.ringcentral.com/api-reference/Internal-Contacts/readDirectoryEntry" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readDirectoryEntry" class="collapse" aria-labelledby="readDirectoryEntry">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of owning account</td>
            </tr>
<tr>
	      <td class="n">entryId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of extension to read information for</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listDirectoryEntries" aria-expanded="true" aria-controls="listDirectoryEntries">Get Company Directory Entries</a> 
        
      </td>
      <td class="description"><p>Returns contact information on corporate users of federated accounts. Please note: 1. <code>User</code>, <code>DigitalUser</code>, <code>VirtualUser</code> and <code>FaxUser</code> types are returned as <code>User</code> type. 2. <code>ApplicationExtension</code> type is not returned. 3. Only extensions in <code>Enabled</code>, <code>Disabled</code> and <code>NotActivated</code> state are returned.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/directory/entries <a href="https://developers.ringcentral.com/api-reference/Internal-Contacts/listDirectoryEntries" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listDirectoryEntries" class="collapse" aria-labelledby="listDirectoryEntries">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">If-None-Match</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">If-None-Match</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">string</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Page number</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">1000</td>
	      <td class="r">False</td>
	      <td class="de">Records count to be returned per one page. The default value is 1000. Specific keyword values: `all` - all records are returned in one page; `max` - maximum count of records that can be returned in one page</td>
            </tr>
<tr>
	      <td class="n">showFederated</td>
	      <td class="t">boolean</td>
	      <td class="d">True</td>
	      <td class="r">False</td>
	      <td class="de">If 'True' then contacts of all accounts in federation are returned. If 'False' then only contacts of the current account are returned, and account section is eliminated in this case</td>
            </tr>
<tr>
	      <td class="n">siteId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of the business site to which extensions belong</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of an extension</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readAccountFederation" aria-expanded="true" aria-controls="readAccountFederation">Get Account Federation</a> 
        
      </td>
      <td class="description"><p>Returns information on a federation and associated accounts.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/directory/federation <a href="https://developers.ringcentral.com/api-reference/Internal-Contacts/readAccountFederation" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAccountFederation" class="collapse" aria-labelledby="readAccountFederation">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">RCExtensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">RCExtensionId</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Meeting Configuration

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readMeetingServiceInfo" aria-expanded="true" aria-controls="readMeetingServiceInfo">Get Meeting Service Info</a> 
        
      </td>
      <td class="description"><p>Returns information on dial-in numbers for meetings, support and international dial-in numbers URIs and meeting account information.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/meeting/service-info <a href="https://developers.ringcentral.com/api-reference/Meeting-Configuration/readMeetingServiceInfo" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readMeetingServiceInfo" class="collapse" aria-labelledby="readMeetingServiceInfo">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateMeetingServiceInfo" aria-expanded="true" aria-controls="updateMeetingServiceInfo">Update Meeting Service Info</a> 
        
      </td>
      <td class="description"><p>Updates personal meeting identifier.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /restapi/v1.0/account/{accountId}/extension/{extensionId}/meeting/service-info <a href="https://developers.ringcentral.com/api-reference/Meeting-Configuration/updateMeetingServiceInfo" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateMeetingServiceInfo" class="collapse" aria-labelledby="updateMeetingServiceInfo">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readAssistants" aria-expanded="true" aria-controls="readAssistants">Get Assistants</a> 
        
      </td>
      <td class="description"><p>Returns assistants information.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/meetings-configuration/assistants <a href="https://developers.ringcentral.com/api-reference/Meeting-Configuration/readAssistants" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAssistants" class="collapse" aria-labelledby="readAssistants">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readAssistedUsers" aria-expanded="true" aria-controls="readAssistedUsers">Get Assisted Users</a> 
        
      </td>
      <td class="description"><p>Returns assisted users information.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/meetings-configuration/assisted <a href="https://developers.ringcentral.com/api-reference/Meeting-Configuration/readAssistedUsers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAssistedUsers" class="collapse" aria-labelledby="readAssistedUsers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Meeting Management

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listMeetings" aria-expanded="true" aria-controls="listMeetings">Get Scheduled Meetings</a> 
        
      </td>
      <td class="description"><p>Returns a list of meetings for a particular extension. The list of meetings does not include meetings of 'Instant' type.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/meeting <a href="https://developers.ringcentral.com/api-reference/Meeting-Management/listMeetings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listMeetings" class="collapse" aria-labelledby="listMeetings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createMeeting" aria-expanded="true" aria-controls="createMeeting">Create Meeting</a> 
        
      </td>
      <td class="description"><p>Creates a new meeting.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/meeting <a href="https://developers.ringcentral.com/api-reference/Meeting-Management/createMeeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createMeeting" class="collapse" aria-labelledby="createMeeting">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readMeeting" aria-expanded="true" aria-controls="readMeeting">Get Meeting Info</a> 
        
      </td>
      <td class="description"><p>Returns a particular meetings details by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/meeting/{meetingId} <a href="https://developers.ringcentral.com/api-reference/Meeting-Management/readMeeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readMeeting" class="collapse" aria-labelledby="readMeeting">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">meetingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral meeting</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateMeeting" aria-expanded="true" aria-controls="updateMeeting">Update Meeting</a> 
        
      </td>
      <td class="description"><p>Modifies a particular meeting.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/meeting/{meetingId} <a href="https://developers.ringcentral.com/api-reference/Meeting-Management/updateMeeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateMeeting" class="collapse" aria-labelledby="updateMeeting">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">meetingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral meeting</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteMeeting" aria-expanded="true" aria-controls="deleteMeeting">Delete Meeting</a> 
        
      </td>
      <td class="description"><p>Deletes a scheduled meeting.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/meeting/{meetingId} <a href="https://developers.ringcentral.com/api-reference/Meeting-Management/deleteMeeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteMeeting" class="collapse" aria-labelledby="deleteMeeting">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">meetingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral meeting</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#endMeeting" aria-expanded="true" aria-controls="endMeeting">End Meeting</a> 
        
      </td>
      <td class="description"><p>Ends a meetings which is in progress.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/meeting/{meetingId}/end <a href="https://developers.ringcentral.com/api-reference/Meeting-Management/endMeeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="endMeeting" class="collapse" aria-labelledby="endMeeting">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">meetingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral meeting</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Meeting Recordings

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listAccountMeetingRecordings" aria-expanded="true" aria-controls="listAccountMeetingRecordings">Get Account Meeting Recordings List</a> 
        
      </td>
      <td class="description"><p>Returns the list of meeting recordings for the current account.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/meeting-recordings <a href="https://developers.ringcentral.com/api-reference/Meeting-Recordings/listAccountMeetingRecordings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listAccountMeetingRecordings" class="collapse" aria-labelledby="listAccountMeetingRecordings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">meetingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a meeting. Either `meetingId` or `meetingStartTime`/`meetingEndTime` can be specified</td>
            </tr>
<tr>
	      <td class="n">meetingStartTimeFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Recordings of meetings started after the time specified will be returned. Either `meetingId` or `meetingStartTime`/`meetingEndTime` can be specified</td>
            </tr>
<tr>
	      <td class="n">meetingStartTimeTo</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Recordings of meetings started before the time specified will be returned. The default value is current time. Either `meetingId` or `meetingStartTime`/`meetingEndTime` can be specified</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Page number</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Number of items per page. The `max` value is supported to indicate the maximum size - 300</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listUserMeetingRecordings" aria-expanded="true" aria-controls="listUserMeetingRecordings">Get User Meeting Recordings List</a> 
        
      </td>
      <td class="description"><p>Returns the list of meetings recordings for the current user.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/meeting-recordings <a href="https://developers.ringcentral.com/api-reference/Meeting-Recordings/listUserMeetingRecordings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listUserMeetingRecordings" class="collapse" aria-labelledby="listUserMeetingRecordings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">meetingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a meeting. Either `meetingId` or `meetingStartTime`/`meetingEndTime` can be specified</td>
            </tr>
<tr>
	      <td class="n">meetingStartTimeFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Recordings of meetings started after the time specified will be returned. Either `meetingId` or `meetingStartTime`/`meetingEndTime` can be specified</td>
            </tr>
<tr>
	      <td class="n">meetingStartTimeTo</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Recordings of meetings started before the time specified will be returned. The default value is current time. Either `meetingId` or `meetingStartTime`/`meetingEndTime` can be specified</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Page number</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Number of items per page. The `max` value is supported to indicate the maximum size - 300</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Message Exports

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createMessageStoreReport" aria-expanded="true" aria-controls="createMessageStoreReport">Create Message Store Report</a> 
        
      </td>
      <td class="description"><p>Creates a task to collect all account messages for a specified time interval.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/message-store-report <a href="https://developers.ringcentral.com/api-reference/Message-Exports/createMessageStoreReport" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createMessageStoreReport" class="collapse" aria-labelledby="createMessageStoreReport">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readMessageStoreReportTask" aria-expanded="true" aria-controls="readMessageStoreReportTask">Get Message Store Report Task</a> 
        
      </td>
      <td class="description"><p>Returns the current status of a task on report creation.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/message-store-report/{taskId} <a href="https://developers.ringcentral.com/api-reference/Message-Exports/readMessageStoreReportTask" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readMessageStoreReportTask" class="collapse" aria-labelledby="readMessageStoreReportTask">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">taskId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readMessageStoreReportArchive" aria-expanded="true" aria-controls="readMessageStoreReportArchive">Get Message Store Report Archive</a> 
        
      </td>
      <td class="description"><p>Returns the created report with message data not including attachments.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/message-store-report/{taskId}/archive <a href="https://developers.ringcentral.com/api-reference/Message-Exports/readMessageStoreReportArchive" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readMessageStoreReportArchive" class="collapse" aria-labelledby="readMessageStoreReportArchive">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">taskId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readMessageStoreReportArchiveContent" aria-expanded="true" aria-controls="readMessageStoreReportArchiveContent">Get Message Store Report Archive Content</a> 
        
      </td>
      <td class="description"><p>Returns one of the report archives with message contents in application/zip format.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/message-store-report/{taskId}/archive/{archiveId} <a href="https://developers.ringcentral.com/api-reference/Message-Exports/readMessageStoreReportArchiveContent" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readMessageStoreReportArchiveContent" class="collapse" aria-labelledby="readMessageStoreReportArchiveContent">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">archiveId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">taskId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Message Store

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listMessages" aria-expanded="true" aria-controls="listMessages">Get Message List</a> 
        
      </td>
      <td class="description"><p>Returns the list of messages from an extension mailbox.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store <a href="https://developers.ringcentral.com/api-reference/Message-Store/listMessages" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listMessages" class="collapse" aria-labelledby="listMessages">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">availability</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Specifies the availability status for the resulting messages. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">conversationId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Specifies the conversation identifier for the resulting messages</td>
            </tr>
<tr>
	      <td class="n">dateFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The start datetime for resulting messages in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is dateTo minus 24 hours</td>
            </tr>
<tr>
	      <td class="n">dateTo</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The end datetime for resulting messages in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is current time</td>
            </tr>
<tr>
	      <td class="n">direction</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The direction for the resulting messages. If not specified, both inbound and outbound messages are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">distinctConversations</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">If 'True', then the latest messages per every conversation ID are returned</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">messageType</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The type of the resulting messages. If not specified, all messages without message type filtering are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">phoneNumber</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The phone number. If specified, messages are returned for this particular phone number only</td>
            </tr>
<tr>
	      <td class="n">readStatus</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The read status for the resulting messages. Multiple values are accepted</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteMessageByFilter" aria-expanded="true" aria-controls="deleteMessageByFilter">Delete Conversation</a> 
        
      </td>
      <td class="description"><p>Deletes conversation(s) by conversation ID(s). Batch request is supported, max number of IDs passed as query/path parameters is 50. Alternative syntax is supported - user converations can be deleted by passing multiple IDs in request body as an array of string, max number of conversation IDs passed in request body is 100. In this case asterisk is used in the path instead of IDs</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store <a href="https://developers.ringcentral.com/api-reference/Message-Store/deleteMessageByFilter" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteMessageByFilter" class="collapse" aria-labelledby="deleteMessageByFilter">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">conversationId</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">dateTo</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Messages received earlier then the date specified will be deleted. The default value is current datetime</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d">All</td>
	      <td class="r">False</td>
	      <td class="de">Type of messages to be deleted</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readMessage" aria-expanded="true" aria-controls="readMessage">Get Message</a> 
        
      </td>
      <td class="description"><p>Returns individual message record(s) by the given message ID(s). The length of inbound messages is unlimited. Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId} <a href="https://developers.ringcentral.com/api-reference/Message-Store/readMessage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readMessage" class="collapse" aria-labelledby="readMessage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">messageId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a message</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateMessage" aria-expanded="true" aria-controls="updateMessage">Update Message List</a> 
        
      </td>
      <td class="description"><p>Updates message(s) by ID(s). Currently only message read status can be updated. Batch request is supported, max number of IDs passed as query/path parameters is 50. Alternative syntax is supported - user messages can be updated by passing multiple IDs in request body as an array of string, max number of IDs passed in request body is 1000. In this case asterisk is used in the path instead of IDs</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId} <a href="https://developers.ringcentral.com/api-reference/Message-Store/updateMessage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateMessage" class="collapse" aria-labelledby="updateMessage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">dateFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">messageId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a message</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteMessage" aria-expanded="true" aria-controls="deleteMessage">Delete Message</a> 
        
      </td>
      <td class="description"><p>Deletes message(s) by the given message ID(s). The first call of this method transfers the message to the 'Delete' status. The second call transfers the deleted message to the 'Purged' status. If it is required to make the message 'Purged' immediately (from the first call), then set the query parameter purge to 'True'.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId} <a href="https://developers.ringcentral.com/api-reference/Message-Store/deleteMessage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteMessage" class="collapse" aria-labelledby="deleteMessage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">conversationId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a message thread</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">messageId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a message</td>
            </tr>
<tr>
	      <td class="n">purge</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">False</td>
	      <td class="de">If the value is 'True', then the message is purged immediately with all the attachments</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readMessageContent" aria-expanded="true" aria-controls="readMessageContent">Get Message Content</a> 
        
      </td>
      <td class="description"><p>Returns a specific message attachment data as media stream.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId}/content/{attachmentId} <a href="https://developers.ringcentral.com/api-reference/Message-Store/readMessageContent" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readMessageContent" class="collapse" aria-labelledby="readMessageContent">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">attachmentId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a message attachment</td>
            </tr>
<tr>
	      <td class="n">contentDisposition</td>
	      <td class="t">string</td>
	      <td class="d">Inline</td>
	      <td class="r">False</td>
	      <td class="de">Content disposition of a response</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">messageId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a message</td>
            </tr>
<tr>
	      <td class="n">Range</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#syncMessages" aria-expanded="true" aria-controls="syncMessages">Sync Messages</a> 
        
      </td>
      <td class="description"><p>Synchronizes messages.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-sync <a href="https://developers.ringcentral.com/api-reference/Message-Store/syncMessages" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="syncMessages" class="collapse" aria-labelledby="syncMessages">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">conversationId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Conversation identifier for the resulting messages. Meaningful for SMS and Pager messages only.</td>
            </tr>
<tr>
	      <td class="n">dateFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The start datetime for resulting messages in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is dateTo minus 24 hours</td>
            </tr>
<tr>
	      <td class="n">dateTo</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The end datetime for resulting messages in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is current time</td>
            </tr>
<tr>
	      <td class="n">direction</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Direction for the resulting messages. If not specified, both inbound and outbound messages are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">distinctConversations</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">If 'True', then the latest messages per every conversation ID are returned</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">messageType</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type for the resulting messages. If not specified, all types of messages are returned. Multiple values are accepted</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Limits the number of records to be returned (works in combination with dateFrom and dateTo if specified)</td>
            </tr>
<tr>
	      <td class="n">syncToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Value of syncToken property of last sync request response</td>
            </tr>
<tr>
	      <td class="n">syncType</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of message synchronization</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Message Store Configuration 
	
      </td>
      <td class="description"><p>Returns message store settings.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/message-store-configuration <a href="https://developers.ringcentral.com/api-reference/Message-Store/readMessageStoreConfiguration" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readMessageStoreConfiguration" class="collapse" aria-labelledby="readMessageStoreConfiguration">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateMessageStoreConfiguration" aria-expanded="true" aria-controls="updateMessageStoreConfiguration">Update Message Store Configuration</a> 
        
      </td>
      <td class="description"><p>Updates message store settings.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/message-store-configuration <a href="https://developers.ringcentral.com/api-reference/Message-Store/updateMessageStoreConfiguration" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateMessageStoreConfiguration" class="collapse" aria-labelledby="updateMessageStoreConfiguration">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### MMS

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createMMS" aria-expanded="true" aria-controls="createMMS">Create MMS Message</a> 
        
      </td>
      <td class="description"><p>Creates and sends media messages. Sending MMS messages simultaneously to different recipients is limited up to 50 requests per minute; relevant for all client applications.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/mms <a href="https://developers.ringcentral.com/api-reference/MMS/createMMS" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createMMS" class="collapse" aria-labelledby="createMMS">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">MMS envelope and content</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Notes

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createChatNote" aria-expanded="true" aria-controls="createChatNote">Create Note</a> 
        
      </td>
      <td class="description"><p>Creates a new note in the specified chat.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/chats/{chatId}/notes <a href="https://developers.ringcentral.com/api-reference/Notes/createChatNote" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createChatNote" class="collapse" aria-labelledby="createChatNote">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a chat to create a note in</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listChatNotes" aria-expanded="true" aria-controls="listChatNotes">Get Chat Notes</a> 
        
      </td>
      <td class="description"><p>Returns the list of notes created in the specified chat.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/chats/{chatId}/notes <a href="https://developers.ringcentral.com/api-reference/Notes/listChatNotes" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listChatNotes" class="collapse" aria-labelledby="listChatNotes">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a chat to fetch notes from.</td>
            </tr>
<tr>
	      <td class="n">creationTimeFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The start datetime for resulting records in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone</td>
            </tr>
<tr>
	      <td class="n">creationTimeTo</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The end datetime for resulting records in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, e.g. 2019-03-10T18:23:45. The default value is Now.</td>
            </tr>
<tr>
	      <td class="n">creatorId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of the user that created the note. Multiple values are supported</td>
            </tr>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Pagination token</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Max number of notes to be fetched by one request; the value range is 1-250.</td>
            </tr>
<tr>
	      <td class="n">status</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Status of notes to be fetched; if not specified all notes are fetched by default.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Note 
	
      </td>
      <td class="description"><p>Returns the specified note(s). It is possible to fetch up to 50 notes per request.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/notes/{noteId} <a href="https://developers.ringcentral.com/api-reference/Notes/readUserNote" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUserNote" class="collapse" aria-labelledby="readUserNote">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#patchNote" aria-expanded="true" aria-controls="patchNote">Update Note</a> 
        
      </td>
      <td class="description"><p>Edits a note. Notes can be edited by any user if posted to a chat the user belongs to.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /restapi/v1.0/glip/notes/{noteId} <a href="https://developers.ringcentral.com/api-reference/Notes/patchNote" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="patchNote" class="collapse" aria-labelledby="patchNote">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">noteId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a note to be updated</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Delete Note 
	
      </td>
      <td class="description"><p>Deletes the specified note.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/glip/notes/{noteId} <a href="https://developers.ringcentral.com/api-reference/Notes/deleteNote" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteNote" class="collapse" aria-labelledby="deleteNote">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Lock Note 
	
      </td>
      <td class="description"><p>Locks a note providing the user with the unique write access for 5 hours.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/notes/{noteId}/lock <a href="https://developers.ringcentral.com/api-reference/Notes/lockNote" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="lockNote" class="collapse" aria-labelledby="lockNote">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Unlock Note 
	
      </td>
      <td class="description"><p>Unlocks a note letting other users edit this note. Once the note is locked (by another user) it cannot be unlocked during 5 hours since the lock datetime.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/notes/{noteId}/unlock <a href="https://developers.ringcentral.com/api-reference/Notes/unlockNote" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="unlockNote" class="collapse" aria-labelledby="unlockNote">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Publish Note 
	
      </td>
      <td class="description"><p>Publishes a note making it visible to other users.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/notes/{noteId}/publish <a href="https://developers.ringcentral.com/api-reference/Notes/publishNote" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="publishNote" class="collapse" aria-labelledby="publishNote">
</div>
      </td>
    </tr>
</tbody>
</table>

### OAuth 2.0

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#authorize" aria-expanded="true" aria-controls="authorize">Authorize</a> 
        
      </td>
      <td class="description"><p>Returns a link to a login page location.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/oauth/authorize <a href="https://developers.ringcentral.com/api-reference/OAuth-2.0/authorize" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="authorize" class="collapse" aria-labelledby="authorize">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accept_language</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">brand_id</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Brand identifier. If it is not provided in request, server will try to determine brand from client app profile. The default value is '1210' - RingCentral US</td>
            </tr>
<tr>
	      <td class="n">client_id</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Identifier (key) of a client application</td>
            </tr>
<tr>
	      <td class="n">code_challenge</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">code_challenge_method</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">display</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Style of login form. The default value is 'page'. The 'popup' and 'touch' values are featured for mobile applications</td>
            </tr>
<tr>
	      <td class="n">localeId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Localization code of a language. Overwrites 'Accept-Language' header value</td>
            </tr>
<tr>
	      <td class="n">nonce</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">prompt</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Specifies which login form will be displayed. Space-separated set of the following values: 'login' - official RingCentral login form, 'sso' - Single Sign-On login form, 'consent' - form to show the requested scope and prompt user for consent. Either 'login' or 'sso' (or both) must be specified. The default value is 'login&sso'</td>
            </tr>
<tr>
	      <td class="n">redirect_uri</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">This is a callback URI which determines where the response is sent. The value of this parameter must exactly match one of the URIs you have provided for your app upon registration</td>
            </tr>
<tr>
	      <td class="n">request</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">request_uri</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">response_type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Determines authorization flow: **code** - Authorization Code, **token** - Implicit Grant</td>
            </tr>
<tr>
	      <td class="n">scope</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">state</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Client state. Returned back to the client at the end of the flow</td>
            </tr>
<tr>
	      <td class="n">ui_locales</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Localization code of a language. Overwrites 'localeId' parameter value</td>
            </tr>
<tr>
	      <td class="n">ui_options</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">User interface options data</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#revokeToken" aria-expanded="true" aria-controls="revokeToken">Revoke Token</a> 
        
      </td>
      <td class="description"><p>Revokes access/refresh token. Requests to this endpoint must be authenticated with HTTP Basic scheme using the application key and application secret as login and password, correspondingly.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/oauth/revoke <a href="https://developers.ringcentral.com/api-reference/OAuth-2.0/revokeToken" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="revokeToken" class="collapse" aria-labelledby="revokeToken">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">client_assertion</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">client_assertion_type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">token</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Active access or refresh token to be revoked</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#getToken" aria-expanded="true" aria-controls="getToken">Get Token</a> 
        
      </td>
      <td class="description"><p>Returns access tokens for making API requests</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/oauth/token <a href="https://developers.ringcentral.com/api-reference/OAuth-2.0/getToken" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="getToken" class="collapse" aria-labelledby="getToken">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">access_token_ttl</td>
	      <td class="t">integer</td>
	      <td class="d">3600</td>
	      <td class="r">False</td>
	      <td class="de">Access token lifetime in seconds</td>
            </tr>
<tr>
	      <td class="n">account_id</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">assertion</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">brand_id</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">client_assertion</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">client_assertion_type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">client_id</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">code</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Authorization code</td>
            </tr>
<tr>
	      <td class="n">code_verifier</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">endpoint_id</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The unique identifier of a client application. If not specified, the previously specified or auto generated value is used by default</td>
            </tr>
<tr>
	      <td class="n">extension</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Optional. Extension short number. If company number is specified as a username, and extension is not specified, the server will attempt to authenticate client as main company administrator</td>
            </tr>
<tr>
	      <td class="n">grant_type</td>
	      <td class="t">string</td>
	      <td class="d">password</td>
	      <td class="r">False</td>
	      <td class="de">Grant type</td>
            </tr>
<tr>
	      <td class="n">partner_account_id</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">password</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">User's password</td>
            </tr>
<tr>
	      <td class="n">pin</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">redirect_uri</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">This is a callback URI which determines where the response is sent. The value of this parameter must exactly match one of the URIs you have provided for your app upon registration</td>
            </tr>
<tr>
	      <td class="n">refresh_token</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Previously issued refresh token. This is the only formData field used for the Refresh Token Flow.</td>
            </tr>
<tr>
	      <td class="n">refresh_token_ttl</td>
	      <td class="t">integer</td>
	      <td class="d">604800</td>
	      <td class="r">False</td>
	      <td class="de">Refresh token lifetime in seconds</td>
            </tr>
<tr>
	      <td class="n">scope</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">List of API permissions to be used with access token. Can be omitted when requesting all permissions defined during the application registration phase</td>
            </tr>
<tr>
	      <td class="n">username</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Phone number linked to an account or extension in E.164 format with or without leading '+' sign</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Pager Messages

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createInternalTextMessage" aria-expanded="true" aria-controls="createInternalTextMessage">Create Internal Text Message</a> 
        
      </td>
      <td class="description"><p>Creates and sends an internal text message.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/company-pager <a href="https://developers.ringcentral.com/api-reference/Pager-Messages/createInternalTextMessage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createInternalTextMessage" class="collapse" aria-labelledby="createInternalTextMessage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Paging Only Groups

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listPagingGroupUsers" aria-expanded="true" aria-controls="listPagingGroupUsers">Get Paging Group Users</a> 
        
      </td>
      <td class="description"><p>Returns the list of users allowed to page this group.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/paging-only-groups/{pagingOnlyGroupId}/users <a href="https://developers.ringcentral.com/api-reference/Paging-Only-Groups/listPagingGroupUsers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listPagingGroupUsers" class="collapse" aria-labelledby="listPagingGroupUsers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">pagingOnlyGroupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listPagingGroupDevices" aria-expanded="true" aria-controls="listPagingGroupDevices">Get Paging Group Devices</a> 
        
      </td>
      <td class="description"><p>Returns the list of paging devices assigned to this group.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/paging-only-groups/{pagingOnlyGroupId}/devices <a href="https://developers.ringcentral.com/api-reference/Paging-Only-Groups/listPagingGroupDevices" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listPagingGroupDevices" class="collapse" aria-labelledby="listPagingGroupDevices">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">pagingOnlyGroupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#assignMultiplePagingGroupUsersDevices" aria-expanded="true" aria-controls="assignMultiplePagingGroupUsersDevices">Assign Paging Group Users and Devices</a> 
        
      </td>
      <td class="description"><p>Adds and/or removes paging group users and devices.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/paging-only-groups/{pagingOnlyGroupId}/bulk-assign <a href="https://developers.ringcentral.com/api-reference/Paging-Only-Groups/assignMultiplePagingGroupUsersDevices" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="assignMultiplePagingGroupUsersDevices" class="collapse" aria-labelledby="assignMultiplePagingGroupUsersDevices">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">pagingOnlyGroupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Phone Numbers

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listExtensionPhoneNumbers" aria-expanded="true" aria-controls="listExtensionPhoneNumbers">Get Extension Phone Number List</a> 
        
      </td>
      <td class="description"><p>Returns the list of phone numbers that are used by a particular extension, and can be filtered by the phone number type. The returned list contains all numbers which are directly mapped to a given extension plus the features and also company-level numbers which may be used when performing different operations on behalf of this extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/phone-number <a href="https://developers.ringcentral.com/api-reference/Phone-Numbers/listExtensionPhoneNumbers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listExtensionPhoneNumbers" class="collapse" aria-labelledby="listExtensionPhoneNumbers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are allowed. Default value is '1'</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items). If not specified, the value is '100' by default</td>
            </tr>
<tr>
	      <td class="n">status</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Status of a phone number. Multiple values are supported</td>
            </tr>
<tr>
	      <td class="n">usageType</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Usage type of a phone number</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listAccountPhoneNumbers" aria-expanded="true" aria-controls="listAccountPhoneNumbers">Get Company Phone Number List</a> 
        
      </td>
      <td class="description"><p>Returns the list of phone numbers assigned to RingCentral customer account. Both company-level and extension-level numbers are returned.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/phone-number <a href="https://developers.ringcentral.com/api-reference/Phone-Numbers/listAccountPhoneNumbers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listAccountPhoneNumbers" class="collapse" aria-labelledby="listAccountPhoneNumbers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">status</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Status of a phone number. Multiple values are supported</td>
            </tr>
<tr>
	      <td class="n">usageType</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Usage type of a phone number</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readAccountPhoneNumber" aria-expanded="true" aria-controls="readAccountPhoneNumber">Get Phone Number</a> 
        
      </td>
      <td class="description"><p>Returns the phone number(s) belonging to a certain account or extension by phoneNumberId(s). Batch request is supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/phone-number/{phoneNumberId} <a href="https://developers.ringcentral.com/api-reference/Phone-Numbers/readAccountPhoneNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAccountPhoneNumber" class="collapse" aria-labelledby="readAccountPhoneNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">phoneNumberId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a phone number</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#parsePhoneNumber" aria-expanded="true" aria-controls="parsePhoneNumber">Parse Phone Number</a> 
        
      </td>
      <td class="description"><p>Returns one or more parsed and/or formatted phone numbers that are passed as a string.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/number-parser/parse <a href="https://developers.ringcentral.com/api-reference/Phone-Numbers/parsePhoneNumber" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="parsePhoneNumber" class="collapse" aria-labelledby="parsePhoneNumber">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">homeCountry</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a home country. The default value is ISO code (ISO 3166) of the user's home country or brand country, if the user is undefined</td>
            </tr>
<tr>
	      <td class="n">nationalAsPriority</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The default value is 'False'. If 'True', the numbers that are closer to the home country are given higher priority</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Posts

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readGlipPost" aria-expanded="true" aria-controls="readGlipPost">Get Post</a> 
        
      </td>
      <td class="description"><p>Returns information about the specified post.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/chats/{chatId}/posts/{postId} <a href="https://developers.ringcentral.com/api-reference/Posts/readGlipPost" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipPost" class="collapse" aria-labelledby="readGlipPost">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a chat.</td>
            </tr>
<tr>
	      <td class="n">postId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a post.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#patchGlipPost" aria-expanded="true" aria-controls="patchGlipPost">Update Post</a> 
        
      </td>
      <td class="description"><p>Updates a specific post within a chat.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /restapi/v1.0/glip/chats/{chatId}/posts/{postId} <a href="https://developers.ringcentral.com/api-reference/Posts/patchGlipPost" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="patchGlipPost" class="collapse" aria-labelledby="patchGlipPost">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a chat.</td>
            </tr>
<tr>
	      <td class="n">postId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a post to be updated.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteGlipPost" aria-expanded="true" aria-controls="deleteGlipPost">Delete Post</a> 
        
      </td>
      <td class="description"><p>Deletes the specified post from the chat.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/glip/chats/{chatId}/posts/{postId} <a href="https://developers.ringcentral.com/api-reference/Posts/deleteGlipPost" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteGlipPost" class="collapse" aria-labelledby="deleteGlipPost">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a chat.</td>
            </tr>
<tr>
	      <td class="n">postId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a post to be deleted.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readGlipPosts" aria-expanded="true" aria-controls="readGlipPosts">Get Posts</a> 
        
      </td>
      <td class="description"><p>Returns a list of posts from the specified chat.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/chats/{chatId}/posts <a href="https://developers.ringcentral.com/api-reference/Posts/readGlipPosts" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipPosts" class="collapse" aria-labelledby="readGlipPosts">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a chat.</td>
            </tr>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Pagination token.</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Max number of posts to be fetched by one request (Not more than 250).</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createGlipPost" aria-expanded="true" aria-controls="createGlipPost">Create Post</a> 
        
      </td>
      <td class="description"><p>Creates a post within the specified chat. Attachments are supported.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/chats/{chatId}/posts <a href="https://developers.ringcentral.com/api-reference/Posts/createGlipPost" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createGlipPost" class="collapse" aria-labelledby="createGlipPost">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a chat.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listGlipGroupPosts" aria-expanded="true" aria-controls="listGlipGroupPosts">Get Group Posts</a> 
        
      </td>
      <td class="description"><p>Returns posts which are available for the current user by group ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/groups/{groupId}/posts <a href="https://developers.ringcentral.com/api-reference/Posts/listGlipGroupPosts" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listGlipGroupPosts" class="collapse" aria-labelledby="listGlipGroupPosts">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a group</td>
            </tr>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Pagination token</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Max number of records to be returned</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createGlipGroupPost" aria-expanded="true" aria-controls="createGlipGroupPost">Create Post in Group</a> 
        
      </td>
      <td class="description"><p>Creates a new post in a group specified.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/groups/{groupId}/posts <a href="https://developers.ringcentral.com/api-reference/Posts/createGlipGroupPost" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createGlipGroupPost" class="collapse" aria-labelledby="createGlipGroupPost">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a group.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateGlipPostText" aria-expanded="true" aria-controls="updateGlipPostText">Update Post</a> 
        
      </td>
      <td class="description"><p>Modifies text of a post.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/glip/groups/{groupId}/posts/{postId}/text <a href="https://developers.ringcentral.com/api-reference/Posts/updateGlipPostText" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateGlipPostText" class="collapse" aria-labelledby="updateGlipPostText">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a group</td>
            </tr>
<tr>
	      <td class="n">postId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a post</td>
            </tr>
<tr>
	      <td class="n">text</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createGlipCard" aria-expanded="true" aria-controls="createGlipCard">Create Card</a> 
        
      </td>
      <td class="description"><p>Creates a new message.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/cards <a href="https://developers.ringcentral.com/api-reference/Posts/createGlipCard" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createGlipCard" class="collapse" aria-labelledby="createGlipCard">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Internal identifier of a group where to create a post with the card</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Card 
	
      </td>
      <td class="description"><p>Returns card(s) with given id(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/cards/{cardId} <a href="https://developers.ringcentral.com/api-reference/Posts/readGlipCard" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipCard" class="collapse" aria-labelledby="readGlipCard">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateGlipCard" aria-expanded="true" aria-controls="updateGlipCard">Update Card</a> 
        
      </td>
      <td class="description"><p>Updates a card.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/glip/cards/{cardId} <a href="https://developers.ringcentral.com/api-reference/Posts/updateGlipCard" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateGlipCard" class="collapse" aria-labelledby="updateGlipCard">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">cardId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a card</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Delete Card 
	
      </td>
      <td class="description"><p>Deletes a card by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/glip/cards/{cardId} <a href="https://developers.ringcentral.com/api-reference/Posts/deleteGlipCard" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteGlipCard" class="collapse" aria-labelledby="deleteGlipCard">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listGlipPosts" aria-expanded="true" aria-controls="listGlipPosts">Get Posts</a> 
        
      </td>
      <td class="description"><p>Returns posts available for the current user by group ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/posts <a href="https://developers.ringcentral.com/api-reference/Posts/listGlipPosts" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listGlipPosts" class="collapse" aria-labelledby="listGlipPosts">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">groupId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Identifier of a group to filter posts</td>
            </tr>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Token of a page to be returned</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Number of records to be returned. The maximum value is 250, by default - 30</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Create Post 
	
      </td>
      <td class="description"><p>Creates a post.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/posts <a href="https://developers.ringcentral.com/api-reference/Posts/createPost" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createPost" class="collapse" aria-labelledby="createPost">
</div>
      </td>
    </tr>
</tbody>
</table>

### Presence

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readUserPresenceStatus" aria-expanded="true" aria-controls="readUserPresenceStatus">Get User Presence Status</a> 
        
      </td>
      <td class="description"><p>Returns presence status of an extension or several extensions by their ID(s). Batch request is supported. The 'presenceStatus' is returned as Offline (the parameters 'telephonyStatus', 'message', 'userStatus' and 'dndStatus' are not returned at all) for the following extension types: Department/Announcement Only/Take Messages Only (Voicemail)/Fax User/Paging Only Group/Shared Lines Group/IVR Menu/Application Extension/Park Location.If the user requests his/her own presence status, the response contains actual presence status even if the status publication is turned off. Batch request is supported. For batch requests the number of extensions in one request is limited to 30. If more extensions are included in the request, the error code 400 Bad Request is returned with the logical error code InvalidMultipartRequest and the corresponding message 'Extension Presence Info multipart request is limited to 30 extensions'.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/presence <a href="https://developers.ringcentral.com/api-reference/Presence/readUserPresenceStatus" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUserPresenceStatus" class="collapse" aria-labelledby="readUserPresenceStatus">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">detailedTelephonyState</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Whether to return detailed telephony state</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">sipData</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Whether to return SIP data</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateUserPresenceStatus" aria-expanded="true" aria-controls="updateUserPresenceStatus">Update User Presence Status</a> 
        
      </td>
      <td class="description"><p>Updates user-defined extension presence status, status message and DnD status by extension ID. Supported for regular User extensions only. The extension types listed do not support presence status: Department, Announcement Only, Take Messages Only (Voicemail), Fax User, Paging Only Group, Shared Lines Group, IVR Menu, Application Extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/presence <a href="https://developers.ringcentral.com/api-reference/Presence/updateUserPresenceStatus" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateUserPresenceStatus" class="collapse" aria-labelledby="updateUserPresenceStatus">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readAccountPresence" aria-expanded="true" aria-controls="readAccountPresence">Get User Presence Status List</a> 
        
      </td>
      <td class="description"><p>Returns presence status of all extensions of an account. Please note: The presenceStatus is returned as Offline (the parameters telephonyStatus, message, userStatus and dndStatus are not returned at all) for the following extension types: Department, Announcement Only, Voicemail (Take Messages Only), Fax User, Paging Only Group, Shared Lines Group, IVR Menu, Application Extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/presence <a href="https://developers.ringcentral.com/api-reference/Presence/readAccountPresence" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAccountPresence" class="collapse" aria-labelledby="readAccountPresence">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">detailedTelephonyState</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Whether to return detailed telephony state</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Page number for account presence information</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Number for account presence information items per page</td>
            </tr>
<tr>
	      <td class="n">sipData</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Whether to return SIP data</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readUnifiedPresence" aria-expanded="true" aria-controls="readUnifiedPresence">Get Unified Presence</a> 
        
      </td>
      <td class="description"><p>Returns the unified presence status of the requested user(s). The set of parameters returned by this method differs whether you return the requester's presence or any other user presence.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/unified-presence <a href="https://developers.ringcentral.com/api-reference/Presence/readUnifiedPresence" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUnifiedPresence" class="collapse" aria-labelledby="readUnifiedPresence">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">None</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">None</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateUnifiedPresence" aria-expanded="true" aria-controls="updateUnifiedPresence">Update Unified Presence</a> 
        
      </td>
      <td class="description"><p>Updates the unified presence for the current user specified in path.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /restapi/v1.0/account/{accountId}/extension/{extensionId}/unified-presence <a href="https://developers.ringcentral.com/api-reference/Presence/updateUnifiedPresence" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateUnifiedPresence" class="collapse" aria-labelledby="updateUnifiedPresence">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">None</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">None</td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Regional Settings

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        Get Language List 
	
      </td>
      <td class="description"><p>Returns the information about supported languages.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/language <a href="https://developers.ringcentral.com/api-reference/Regional-Settings/listLanguages" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listLanguages" class="collapse" aria-labelledby="listLanguages">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Language 
	
      </td>
      <td class="description"><p>Returns language by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/language/{languageId} <a href="https://developers.ringcentral.com/api-reference/Regional-Settings/readLanguage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readLanguage" class="collapse" aria-labelledby="readLanguage">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listCountries" aria-expanded="true" aria-controls="listCountries">Get Country List</a> 
        
      </td>
      <td class="description"><p>Returns all the countries available for calling.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/country <a href="https://developers.ringcentral.com/api-reference/Regional-Settings/listCountries" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCountries" class="collapse" aria-labelledby="listCountries">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">freeSoftphoneLine</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Specifies if free phone line for softphone is available for a country or not</td>
            </tr>
<tr>
	      <td class="n">loginAllowed</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Specifies whether login with the phone numbers of this country is enabled or not</td>
            </tr>
<tr>
	      <td class="n">numberSelling</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Specifies if RingCentral sells phone numbers of this country</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">signupAllowed</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Indicates whether signup/billing is allowed for a country. If not specified all countries are returned (according to other filters specified if any)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Country 
	
      </td>
      <td class="description"><p>Returns the information on a specific country.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/country/{countryId} <a href="https://developers.ringcentral.com/api-reference/Regional-Settings/readCountry" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCountry" class="collapse" aria-labelledby="readCountry">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listLocations" aria-expanded="true" aria-controls="listLocations">Get Location List</a> 
        
      </td>
      <td class="description"><p>Returns all available locations for a certain state.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/location <a href="https://developers.ringcentral.com/api-reference/Regional-Settings/listLocations" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listLocations" class="collapse" aria-labelledby="listLocations">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">orderBy</td>
	      <td class="t">string</td>
	      <td class="d">City</td>
	      <td class="r">False</td>
	      <td class="de">Sorts results by the property specified</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">stateId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a state</td>
            </tr>
<tr>
	      <td class="n">withNxx</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Specifies if nxx codes are returned</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listStates" aria-expanded="true" aria-controls="listStates">Get States List</a> 
        
      </td>
      <td class="description"><p>Returns all the states of a certain country</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/state <a href="https://developers.ringcentral.com/api-reference/Regional-Settings/listStates" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listStates" class="collapse" aria-labelledby="listStates">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">allCountries</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">If set to 'True' then states for all countries are returned and `countryId` is ignored, even if specified. If the value is empty then the parameter is ignored</td>
            </tr>
<tr>
	      <td class="n">countryId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a country</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">withPhoneNumbers</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">False</td>
	      <td class="de">If 'True', the list of states with phone numbers available for buying is returned</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get State 
	
      </td>
      <td class="description"><p>Returns the information on a specific state.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/state/{stateId} <a href="https://developers.ringcentral.com/api-reference/Regional-Settings/readState" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readState" class="collapse" aria-labelledby="readState">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listTimezones" aria-expanded="true" aria-controls="listTimezones">Get Timezone List</a> 
        
      </td>
      <td class="description"><p>Returns all available timezones.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/timezone <a href="https://developers.ringcentral.com/api-reference/Regional-Settings/listTimezones" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listTimezones" class="collapse" aria-labelledby="listTimezones">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">page</td>
	      <td class="t">string</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">string</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readTimezone" aria-expanded="true" aria-controls="readTimezone">Get Timezone</a> 
        
      </td>
      <td class="description"><p>Returns the information on a certain timezone.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/timezone/{timezoneId} <a href="https://developers.ringcentral.com/api-reference/Regional-Settings/readTimezone" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readTimezone" class="collapse" aria-labelledby="readTimezone">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">page</td>
	      <td class="t">string</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">string</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items)</td>
            </tr>
<tr>
	      <td class="n">timezoneId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a timezone</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### RingOut

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createRingOutCall" aria-expanded="true" aria-controls="createRingOutCall">Make RingOut Call</a> 
        
      </td>
      <td class="description"><p>Makes a 2-leg RingOut call.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/ring-out <a href="https://developers.ringcentral.com/api-reference/RingOut/createRingOutCall" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createRingOutCall" class="collapse" aria-labelledby="createRingOutCall">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readRingOutCallStatus" aria-expanded="true" aria-controls="readRingOutCallStatus">Get RingOut Call Status</a> 
        
      </td>
      <td class="description"><p>Returns the status of a 2-leg RingOut call.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/ring-out/{ringoutId} <a href="https://developers.ringcentral.com/api-reference/RingOut/readRingOutCallStatus" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readRingOutCallStatus" class="collapse" aria-labelledby="readRingOutCallStatus">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">ringoutId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingOut call</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteRingOutCall" aria-expanded="true" aria-controls="deleteRingOutCall">Cancel RingOut Call</a> 
        
      </td>
      <td class="description"><p>Cancels a 2-leg RingOut call.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/ring-out/{ringoutId} <a href="https://developers.ringcentral.com/api-reference/RingOut/deleteRingOutCall" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteRingOutCall" class="collapse" aria-labelledby="deleteRingOutCall">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">ringoutId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingOut call</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createRingOutCallDeprecated" aria-expanded="true" aria-controls="createRingOutCallDeprecated">Make RingOut Call</a> 
        
      </td>
      <td class="description"><p>Makes a 2-leg RingOut call.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/ringout <a href="https://developers.ringcentral.com/api-reference/RingOut/createRingOutCallDeprecated" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createRingOutCallDeprecated" class="collapse" aria-labelledby="createRingOutCallDeprecated">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readRingOutCallStatusDeprecated" aria-expanded="true" aria-controls="readRingOutCallStatusDeprecated">Get RingOut Call Status</a> 
        
      </td>
      <td class="description"><p>Returns status of a 2-leg RingOut call.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/ringout/{ringoutId} <a href="https://developers.ringcentral.com/api-reference/RingOut/readRingOutCallStatusDeprecated" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readRingOutCallStatusDeprecated" class="collapse" aria-labelledby="readRingOutCallStatusDeprecated">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">ringoutId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingOut call</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteRingOutCallDeprecated" aria-expanded="true" aria-controls="deleteRingOutCallDeprecated">Cancel RingOut Call</a> 
        
      </td>
      <td class="description"><p>Cancels a 2-leg RingOut call.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/ringout/{ringoutId} <a href="https://developers.ringcentral.com/api-reference/RingOut/deleteRingOutCallDeprecated" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteRingOutCallDeprecated" class="collapse" aria-labelledby="deleteRingOutCallDeprecated">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">ringoutId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingOut call</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Rule Management

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listAnsweringRules" aria-expanded="true" aria-controls="listAnsweringRules">Get Call Handling Rules</a> 
        
      </td>
      <td class="description"><p>Returns the extension answering rules.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule <a href="https://developers.ringcentral.com/api-reference/Rule-Management/listAnsweringRules" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listAnsweringRules" class="collapse" aria-labelledby="listAnsweringRules">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">enabledOnly</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">False</td>
	      <td class="de">If true, then only active call handling rules are returned</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">string</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">string</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">view</td>
	      <td class="t">string</td>
	      <td class="d">Simple</td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createAnsweringRule" aria-expanded="true" aria-controls="createAnsweringRule">Create Call Handling Rule</a> 
        
      </td>
      <td class="description"><p>Creates a custom answering rule for a particular caller ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule <a href="https://developers.ringcentral.com/api-reference/Rule-Management/createAnsweringRule" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createAnsweringRule" class="collapse" aria-labelledby="createAnsweringRule">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readAnsweringRule" aria-expanded="true" aria-controls="readAnsweringRule">Get Call Handling Rule</a> 
        
      </td>
      <td class="description"><p>Returns an answering rule by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule/{ruleId} <a href="https://developers.ringcentral.com/api-reference/Rule-Management/readAnsweringRule" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAnsweringRule" class="collapse" aria-labelledby="readAnsweringRule">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">ruleId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an answering rule. The value can be standard digital ID or specific ID - either 'business-hours-rule' or 'after-hours-rule'</td>
            </tr>
<tr>
	      <td class="n">showInactiveNumbers</td>
	      <td class="t">boolean</td>
	      <td class="d">False</td>
	      <td class="r">False</td>
	      <td class="de">Indicates whether inactive numbers should be returned or not</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateAnsweringRule" aria-expanded="true" aria-controls="updateAnsweringRule">Update Call Handling Rule</a> 
        
      </td>
      <td class="description"><p>Updates a custom answering rule for a particular caller ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule/{ruleId} <a href="https://developers.ringcentral.com/api-reference/Rule-Management/updateAnsweringRule" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateAnsweringRule" class="collapse" aria-labelledby="updateAnsweringRule">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">ruleId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an answering rule</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteAnsweringRule" aria-expanded="true" aria-controls="deleteAnsweringRule">Delete Call Handling Rule</a> 
        
      </td>
      <td class="description"><p>Deletes a custom answering rule by a particular ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule/{ruleId} <a href="https://developers.ringcentral.com/api-reference/Rule-Management/deleteAnsweringRule" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteAnsweringRule" class="collapse" aria-labelledby="deleteAnsweringRule">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">ruleId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an answering rule</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createCompanyAnsweringRule" aria-expanded="true" aria-controls="createCompanyAnsweringRule">Create Company Call Handling Rule</a> 
        
      </td>
      <td class="description"><p>Creates a company answering rule for a particular caller ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/answering-rule <a href="https://developers.ringcentral.com/api-reference/Rule-Management/createCompanyAnsweringRule" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createCompanyAnsweringRule" class="collapse" aria-labelledby="createCompanyAnsweringRule">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listCompanyAnsweringRules" aria-expanded="true" aria-controls="listCompanyAnsweringRules">Get Company Call Handling Rule List</a> 
        
      </td>
      <td class="description"><p>Returns a list of company answering rules.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/answering-rule <a href="https://developers.ringcentral.com/api-reference/Rule-Management/listCompanyAnsweringRules" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCompanyAnsweringRules" class="collapse" aria-labelledby="listCompanyAnsweringRules">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items per page)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readCompanyAnsweringRule" aria-expanded="true" aria-controls="readCompanyAnsweringRule">Get Company Call Handling Rule</a> 
        
      </td>
      <td class="description"><p>Returns a company answering rule by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/answering-rule/{ruleId} <a href="https://developers.ringcentral.com/api-reference/Rule-Management/readCompanyAnsweringRule" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCompanyAnsweringRule" class="collapse" aria-labelledby="readCompanyAnsweringRule">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">ruleId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an answering rule. The value can be standard digital ID or specific ID - either 'business-hours-rule' or 'after-hours-rule'</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateCompanyAnsweringRule" aria-expanded="true" aria-controls="updateCompanyAnsweringRule">Update Company Call Handling Rule</a> 
        
      </td>
      <td class="description"><p>Updates a company answering rule.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/answering-rule/{ruleId} <a href="https://developers.ringcentral.com/api-reference/Rule-Management/updateCompanyAnsweringRule" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateCompanyAnsweringRule" class="collapse" aria-labelledby="updateCompanyAnsweringRule">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">ruleId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an answering rule. The value can be standard digital ID or specific ID - either 'business-hours-rule' or 'after-hours-rule'</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteCompanyAnsweringRule" aria-expanded="true" aria-controls="deleteCompanyAnsweringRule">Delete Company Call Handling Rule</a> 
        
      </td>
      <td class="description"><p>Deletes a company custom answering rule by a particular ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/answering-rule/{ruleId} <a href="https://developers.ringcentral.com/api-reference/Rule-Management/deleteCompanyAnsweringRule" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteCompanyAnsweringRule" class="collapse" aria-labelledby="deleteCompanyAnsweringRule">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">ruleId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an answering rule</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listStandardGreetings" aria-expanded="true" aria-controls="listStandardGreetings">Get Standard Greeting List</a> 
        
      </td>
      <td class="description"><p>Returns the list of predefined standard greetings. Custom greetings recorded by user are not returned in response to this request. See Get Extension Custom Greetings.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/greeting <a href="https://developers.ringcentral.com/api-reference/Rule-Management/listStandardGreetings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listStandardGreetings" class="collapse" aria-labelledby="listStandardGreetings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">page</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page number to retrieve. Only positive number values are accepted.</td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">Indicates the page size (number of items).</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of a greeting, specifying the case when the greeting is played</td>
            </tr>
<tr>
	      <td class="n">usageType</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Usage type of a greeting, specifying if the greeting is applied for user extension or department extension</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Standard Greeting 
	
      </td>
      <td class="description"><p>Returns a standard greeting by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/dictionary/greeting/{greetingId} <a href="https://developers.ringcentral.com/api-reference/Rule-Management/readStandardGreeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readStandardGreeting" class="collapse" aria-labelledby="readStandardGreeting">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createCompanyGreeting" aria-expanded="true" aria-controls="createCompanyGreeting">Create Company Greeting</a> 
        
      </td>
      <td class="description"><p>Creates a custom company greeting.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/greeting <a href="https://developers.ringcentral.com/api-reference/Rule-Management/createCompanyGreeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createCompanyGreeting" class="collapse" aria-labelledby="createCompanyGreeting">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">answeringRuleId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Internal identifier of an answering rule</td>
            </tr>
<tr>
	      <td class="n">binary</td>
	      <td class="t">file</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Meida file to upload</td>
            </tr>
<tr>
	      <td class="n">languageId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de">Internal identifier of a language. See Get Language List</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Type of a greeting, specifying the case when the greeting is played.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createCustomUserGreeting" aria-expanded="true" aria-controls="createCustomUserGreeting">Create Custom User Greeting</a> 
        
      </td>
      <td class="description"><p>Creates custom greeting for an extension user.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/greeting <a href="https://developers.ringcentral.com/api-reference/Rule-Management/createCustomUserGreeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createCustomUserGreeting" class="collapse" aria-labelledby="createCustomUserGreeting">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">answeringRuleId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an answering rule</td>
            </tr>
<tr>
	      <td class="n">binary</td>
	      <td class="t">file</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Meida file to upload</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Type of a greeting, specifying the case when the greeting is played.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readCustomGreeting" aria-expanded="true" aria-controls="readCustomGreeting">Get Custom Greeting</a> 
        
      </td>
      <td class="description"><p>Returns a custom user greeting by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/greeting/{greetingId} <a href="https://developers.ringcentral.com/api-reference/Rule-Management/readCustomGreeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCustomGreeting" class="collapse" aria-labelledby="readCustomGreeting">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">greetingId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a greeting</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Call Recording Settings 
	
      </td>
      <td class="description"><p>Returns call recording settings.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-recording <a href="https://developers.ringcentral.com/api-reference/Rule-Management/readCallRecordingSettings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readCallRecordingSettings" class="collapse" aria-labelledby="readCallRecordingSettings">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateCallRecordingSettings" aria-expanded="true" aria-controls="updateCallRecordingSettings">Update Call Recording Settings</a> 
        
      </td>
      <td class="description"><p>Updates current call recording settings.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/call-recording <a href="https://developers.ringcentral.com/api-reference/Rule-Management/updateCallRecordingSettings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateCallRecordingSettings" class="collapse" aria-labelledby="updateCallRecordingSettings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">false</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Call Recording Extension List 
	
      </td>
      <td class="description"><p>Returns the list of extensions to be recorded.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-recording/extensions <a href="https://developers.ringcentral.com/api-reference/Rule-Management/listCallRecordingExtensions" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCallRecordingExtensions" class="collapse" aria-labelledby="listCallRecordingExtensions">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateCallRecordingExtensionList" aria-expanded="true" aria-controls="updateCallRecordingExtensionList">Update Call Recording Extension List</a> 
        
      </td>
      <td class="description"><p>Creates or updates the list of extensions to be recorded.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/call-recording/bulk-assign <a href="https://developers.ringcentral.com/api-reference/Rule-Management/updateCallRecordingExtensionList" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateCallRecordingExtensionList" class="collapse" aria-labelledby="updateCallRecordingExtensionList">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listCallRecordingCustomGreetings" aria-expanded="true" aria-controls="listCallRecordingCustomGreetings">Get Call Recording Custom Greeting List</a> 
        
      </td>
      <td class="description"><p>Returns call recording custom greetings.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/call-recording/custom-greetings <a href="https://developers.ringcentral.com/api-reference/Rule-Management/listCallRecordingCustomGreetings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listCallRecordingCustomGreetings" class="collapse" aria-labelledby="listCallRecordingCustomGreetings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">type</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Delete Call Recording Custom Greeting List 
	
      </td>
      <td class="description"><p>Deletes call recording custom greetings.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/call-recording/custom-greetings <a href="https://developers.ringcentral.com/api-reference/Rule-Management/deleteCallRecordingCustomGreetingList" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteCallRecordingCustomGreetingList" class="collapse" aria-labelledby="deleteCallRecordingCustomGreetingList">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteCallRecordingCustomGreeting" aria-expanded="true" aria-controls="deleteCallRecordingCustomGreeting">Delete Call Recording Custom Greeting</a> 
        
      </td>
      <td class="description"><p>Deletes call recording custom greeting(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/call-recording/custom-greetings/{greetingId} <a href="https://developers.ringcentral.com/api-reference/Rule-Management/deleteCallRecordingCustomGreeting" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteCallRecordingCustomGreeting" class="collapse" aria-labelledby="deleteCallRecordingCustomGreeting">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">greetingId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### SCIM

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        Check Health 
	
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /scim/health <a href="https://developers.ringcentral.com/api-reference/SCIM/checkHealth" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="checkHealth" class="collapse" aria-labelledby="checkHealth">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Check Health 
	
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /scim/v2/health <a href="https://developers.ringcentral.com/api-reference/SCIM/checkHealth2" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="checkHealth2" class="collapse" aria-labelledby="checkHealth2">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Service Provider Config 
	
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /scim/v2/ServiceProviderConfig <a href="https://developers.ringcentral.com/api-reference/SCIM/readServiceProviderConfig2" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readServiceProviderConfig2" class="collapse" aria-labelledby="readServiceProviderConfig2">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Service Provider Config 
	
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /scim/ServiceProviderConfig <a href="https://developers.ringcentral.com/api-reference/SCIM/readServiceProviderConfig" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readServiceProviderConfig" class="collapse" aria-labelledby="readServiceProviderConfig">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#searchViaGet2" aria-expanded="true" aria-controls="searchViaGet2">Search/List Users</a> 
        
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /scim/v2/Users <a href="https://developers.ringcentral.com/api-reference/SCIM/searchViaGet2" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="searchViaGet2" class="collapse" aria-labelledby="searchViaGet2">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">count</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">page size</td>
            </tr>
<tr>
	      <td class="n">filter</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">only support 'userName' or 'email' filter expressions for now</td>
            </tr>
<tr>
	      <td class="n">startIndex</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">start index (1-based)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Create User 
	
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /scim/v2/Users <a href="https://developers.ringcentral.com/api-reference/SCIM/createUser2" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createUser2" class="collapse" aria-labelledby="createUser2">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#searchViaGet" aria-expanded="true" aria-controls="searchViaGet">Search/List Users</a> 
        
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /scim/Users <a href="https://developers.ringcentral.com/api-reference/SCIM/searchViaGet" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="searchViaGet" class="collapse" aria-labelledby="searchViaGet">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">count</td>
	      <td class="t">integer</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de">page size</td>
            </tr>
<tr>
	      <td class="n">filter</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">only support 'userName' or 'email' filter expressions for now</td>
            </tr>
<tr>
	      <td class="n">startIndex</td>
	      <td class="t">integer</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de">start index (1-based)</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Create User 
	
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /scim/Users <a href="https://developers.ringcentral.com/api-reference/SCIM/createUser" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createUser" class="collapse" aria-labelledby="createUser">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Search/List Users 
	
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /scim/v2/Users/.search <a href="https://developers.ringcentral.com/api-reference/SCIM/searchViaPost2" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="searchViaPost2" class="collapse" aria-labelledby="searchViaPost2">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get User 
	
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /scim/v2/Users/{id} <a href="https://developers.ringcentral.com/api-reference/SCIM/readUser2" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUser2" class="collapse" aria-labelledby="readUser2">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#replaceUser2" aria-expanded="true" aria-controls="replaceUser2">Update/Replace User</a> 
        
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /scim/v2/Users/{id} <a href="https://developers.ringcentral.com/api-reference/SCIM/replaceUser2" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="replaceUser2" class="collapse" aria-labelledby="replaceUser2">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">an existing user</td>
            </tr>
<tr>
	      <td class="n">id</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">user id</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Delete User 
	
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /scim/v2/Users/{id} <a href="https://developers.ringcentral.com/api-reference/SCIM/deleteUser2" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteUser2" class="collapse" aria-labelledby="deleteUser2">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#patchUser2" aria-expanded="true" aria-controls="patchUser2">Update/Patch User</a> 
        
      </td>
      <td class="description"></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /scim/v2/Users/{id} <a href="https://developers.ringcentral.com/api-reference/SCIM/patchUser2" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="patchUser2" class="collapse" aria-labelledby="patchUser2">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">patch operations list</td>
            </tr>
<tr>
	      <td class="n">id</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">user id</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### SIP

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        Register SIP Device 
	
      </td>
      <td class="description"><p>Creates SIP registration of a device/application (WebPhone, Mobile, softphone)</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/client-info/sip-provision <a href="https://developers.ringcentral.com/api-reference/SIP/createSIPRegistration" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createSIPRegistration" class="collapse" aria-labelledby="createSIPRegistration">
</div>
      </td>
    </tr>
</tbody>
</table>

### SMS

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createSMSMessage" aria-expanded="true" aria-controls="createSMSMessage">Send SMS</a> 
        
      </td>
      <td class="description"><p>Creates and sends a new text message. You can send SMS messages simultaneously to different recipients up to 40 requests per minute; this limitation is relevant for all client applications. Sending and receiving SMS is available for Toll-Free Numbers within the USA. You can send up to 10 attachments in one MMS message; the size of all attachments linked is limited to 1500000 bytes.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/sms <a href="https://developers.ringcentral.com/api-reference/SMS/createSMSMessage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createSMSMessage" class="collapse" aria-labelledby="createSMSMessage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Subscriptions

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        Get Subscriptions 
	
      </td>
      <td class="description"><p>Returns a list of subscriptions created by a particular user on a particular client app.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/subscription <a href="https://developers.ringcentral.com/api-reference/Subscriptions/listSubscriptions" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listSubscriptions" class="collapse" aria-labelledby="listSubscriptions">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Create Subscription 
	
      </td>
      <td class="description"><p>Creates a new subscription.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/subscription <a href="https://developers.ringcentral.com/api-reference/Subscriptions/createSubscription" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createSubscription" class="collapse" aria-labelledby="createSubscription">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Subscription 
	
      </td>
      <td class="description"><p>Returns the requested subscription.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/subscription/{subscriptionId} <a href="https://developers.ringcentral.com/api-reference/Subscriptions/readSubscription" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readSubscription" class="collapse" aria-labelledby="readSubscription">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateSubscription" aria-expanded="true" aria-controls="updateSubscription">Renew Subscription / Update Event Filters</a> 
        
      </td>
      <td class="description"><p>Renews the existent subscription if the request body is empty. If event filters are specified, calling this method modifies the event filters for the existing subscription. The client application can extend or narrow the events for which it receives notifications in the frame of one subscription.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/subscription/{subscriptionId} <a href="https://developers.ringcentral.com/api-reference/Subscriptions/updateSubscription" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateSubscription" class="collapse" aria-labelledby="updateSubscription">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">aggregated</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">If 'True' then aggregated presence status is returned in a notification payload</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">subscriptionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a subscription</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Cancel Subscription 
	
      </td>
      <td class="description"><p>Cancels the existent subscription.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/subscription/{subscriptionId} <a href="https://developers.ringcentral.com/api-reference/Subscriptions/deleteSubscription" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteSubscription" class="collapse" aria-labelledby="deleteSubscription">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Renew Subscription 
	
      </td>
      <td class="description"><p>Renews an existent subscription by ID by posting request with an empty body.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/subscription/{subscriptionId}/renew <a href="https://developers.ringcentral.com/api-reference/Subscriptions/renewSubscription" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="renewSubscription" class="collapse" aria-labelledby="renewSubscription">
</div>
      </td>
    </tr>
</tbody>
</table>

### Tasks

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listChatTasks" aria-expanded="true" aria-controls="listChatTasks">Get Chat Tasks</a> 
        
      </td>
      <td class="description"><p>Returns the list of tasks of the specified chat.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/chats/{chatId}/tasks <a href="https://developers.ringcentral.com/api-reference/Tasks/listChatTasks" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listChatTasks" class="collapse" aria-labelledby="listChatTasks">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">assigneeId</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a task assignee</td>
            </tr>
<tr>
	      <td class="n">assigneeStatus</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Task execution status by assignee(-s) specified in assigneeId</td>
            </tr>
<tr>
	      <td class="n">assignmentStatus</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Task assignment status</td>
            </tr>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a chat</td>
            </tr>
<tr>
	      <td class="n">creationTimeFrom</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">The start datetime for resulting records in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, e.g. 2016-02-23T00:00:00</td>
            </tr>
<tr>
	      <td class="n">creationTimeTo</td>
	      <td class="t">string</td>
	      <td class="d">now</td>
	      <td class="r">False</td>
	      <td class="de">The end datetime for resulting records in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, e.g. 2019-03-10T18:23:45Z</td>
            </tr>
<tr>
	      <td class="n">creatorId</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a task creator</td>
            </tr>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Token of the current page. If token is omitted then the first page should be returned</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Number of records to be returned per screen</td>
            </tr>
<tr>
	      <td class="n">status</td>
	      <td class="t">array</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Task execution status</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createTask" aria-expanded="true" aria-controls="createTask">Create Task</a> 
        
      </td>
      <td class="description"><p>Creates a task in the specified chat.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/chats/{chatId}/tasks <a href="https://developers.ringcentral.com/api-reference/Tasks/createTask" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createTask" class="collapse" aria-labelledby="createTask">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a chat</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Task 
	
      </td>
      <td class="description"><p>Returns information about the specified task(s) by ID(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/tasks/{taskId} <a href="https://developers.ringcentral.com/api-reference/Tasks/readTask" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readTask" class="collapse" aria-labelledby="readTask">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#patchTask" aria-expanded="true" aria-controls="patchTask">Patch Task</a> 
        
      </td>
      <td class="description"><p>Updates the specified task by ID.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /restapi/v1.0/glip/tasks/{taskId} <a href="https://developers.ringcentral.com/api-reference/Tasks/patchTask" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="patchTask" class="collapse" aria-labelledby="patchTask">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">taskId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a task</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Delete Task 
	
      </td>
      <td class="description"><p>Deletes the specified task.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/glip/tasks/{taskId} <a href="https://developers.ringcentral.com/api-reference/Tasks/deleteTask" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteTask" class="collapse" aria-labelledby="deleteTask">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#completeTask" aria-expanded="true" aria-controls="completeTask">Complete Task</a> 
        
      </td>
      <td class="description"><p>Completes a task in the specified chat.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/tasks/{taskId}/complete <a href="https://developers.ringcentral.com/api-reference/Tasks/completeTask" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="completeTask" class="collapse" aria-labelledby="completeTask">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">taskId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a task</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Teams

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listGlipTeams" aria-expanded="true" aria-controls="listGlipTeams">Get Teams</a> 
        
      </td>
      <td class="description"><p>Returns the list of teams where the user is a member (both archived and active) combined with a list of public teams that can be joined by the current user. All records in response are sorted by creation time of a chat in ascending order.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/teams <a href="https://developers.ringcentral.com/api-reference/Teams/listGlipTeams" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listGlipTeams" class="collapse" aria-labelledby="listGlipTeams">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">pageToken</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Pagination token.</td>
            </tr>
<tr>
	      <td class="n">recordCount</td>
	      <td class="t">integer</td>
	      <td class="d">30</td>
	      <td class="r">False</td>
	      <td class="de">Number of teams to be fetched by one request. The maximum value is 250, by default - 30</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Create Team 
	
      </td>
      <td class="description"><p>Creates a team, and adds a list of people to the team.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/teams <a href="https://developers.ringcentral.com/api-reference/Teams/createGlipTeam" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createGlipTeam" class="collapse" aria-labelledby="createGlipTeam">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Team 
	
      </td>
      <td class="description"><p>Returns information about the specified team.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/teams/{chatId} <a href="https://developers.ringcentral.com/api-reference/Teams/readGlipTeam" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipTeam" class="collapse" aria-labelledby="readGlipTeam">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#patchGlipTeam" aria-expanded="true" aria-controls="patchGlipTeam">Update Team</a> 
        
      </td>
      <td class="description"><p>Updates the name and description of the specified team.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /restapi/v1.0/glip/teams/{chatId} <a href="https://developers.ringcentral.com/api-reference/Teams/patchGlipTeam" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="patchGlipTeam" class="collapse" aria-labelledby="patchGlipTeam">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a team to be updated.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Delete Team 
	
      </td>
      <td class="description"><p>Deletes the specified team.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/glip/teams/{chatId} <a href="https://developers.ringcentral.com/api-reference/Teams/deleteGlipTeam" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteGlipTeam" class="collapse" aria-labelledby="deleteGlipTeam">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Join Team 
	
      </td>
      <td class="description"><p>Adds the current user to the specified team.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/teams/{chatId}/join <a href="https://developers.ringcentral.com/api-reference/Teams/joinGlipTeam" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="joinGlipTeam" class="collapse" aria-labelledby="joinGlipTeam">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Leave Team 
	
      </td>
      <td class="description"><p>Removes the current user from the specified team.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/teams/{chatId}/leave <a href="https://developers.ringcentral.com/api-reference/Teams/leaveGlipTeam" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="leaveGlipTeam" class="collapse" aria-labelledby="leaveGlipTeam">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#addGlipTeamMembers" aria-expanded="true" aria-controls="addGlipTeamMembers">Add Team Members</a> 
        
      </td>
      <td class="description"><p>Adds members to the specified team.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/teams/{chatId}/add <a href="https://developers.ringcentral.com/api-reference/Teams/addGlipTeamMembers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="addGlipTeamMembers" class="collapse" aria-labelledby="addGlipTeamMembers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a team to add members to.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#removeGlipTeamMembers" aria-expanded="true" aria-controls="removeGlipTeamMembers">Remove Team Members</a> 
        
      </td>
      <td class="description"><p>Removes members from the specified team.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/teams/{chatId}/remove <a href="https://developers.ringcentral.com/api-reference/Teams/removeGlipTeamMembers" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="removeGlipTeamMembers" class="collapse" aria-labelledby="removeGlipTeamMembers">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">chatId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a team to remove members from.</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Archive Team 
	
      </td>
      <td class="description"><p>Changes the status of the specified team to 'Archived'.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/teams/{chatId}/archive <a href="https://developers.ringcentral.com/api-reference/Teams/archiveGlipTeam" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="archiveGlipTeam" class="collapse" aria-labelledby="archiveGlipTeam">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Unarchive Team 
	
      </td>
      <td class="description"><p>Changes the status of the specified team to 'Active'.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/glip/teams/{chatId}/unarchive <a href="https://developers.ringcentral.com/api-reference/Teams/unarchiveGlipTeam" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="unarchiveGlipTeam" class="collapse" aria-labelledby="unarchiveGlipTeam">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Get Everyone Chat 
	
      </td>
      <td class="description"><p>Returns information about Everyone chat.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/glip/everyone <a href="https://developers.ringcentral.com/api-reference/Teams/readGlipEveryone" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readGlipEveryone" class="collapse" aria-labelledby="readGlipEveryone">
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        Update Everyone Сhat 
	
      </td>
      <td class="description"><p>Updates Everyone chat information.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PATCH /restapi/v1.0/glip/everyone <a href="https://developers.ringcentral.com/api-reference/Teams/patchGlipEveryone" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="patchGlipEveryone" class="collapse" aria-labelledby="patchGlipEveryone">
</div>
      </td>
    </tr>
</tbody>
</table>

### User Permissions

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readAuthorizationProfile" aria-expanded="true" aria-controls="readAuthorizationProfile">Get Authorization Profile</a> 
        
      </td>
      <td class="description"><p>Returns a list of user permissions granted at authorization procedure. Please note: Some permissions may be restricted by extension type.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/authz-profile <a href="https://developers.ringcentral.com/api-reference/User-Permissions/readAuthorizationProfile" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readAuthorizationProfile" class="collapse" aria-labelledby="readAuthorizationProfile">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#checkUserPermission" aria-expanded="true" aria-controls="checkUserPermission">Check User Permission</a> 
        
      </td>
      <td class="description"><p>Checks if a certain user permission is activated for a particular extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/authz-profile/check <a href="https://developers.ringcentral.com/api-reference/User-Permissions/checkUserPermission" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="checkUserPermission" class="collapse" aria-labelledby="checkUserPermission">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">permissionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">targetExtensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### User Settings

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readExtension" aria-expanded="true" aria-controls="readExtension">Get Extension</a> 
        
      </td>
      <td class="description"><p>Returns basic information about a particular extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId} <a href="https://developers.ringcentral.com/api-reference/User-Settings/readExtension" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readExtension" class="collapse" aria-labelledby="readExtension">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateExtension" aria-expanded="true" aria-controls="updateExtension">Update Extension</a> 
        
      </td>
      <td class="description"><p>Updates user settings.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId} <a href="https://developers.ringcentral.com/api-reference/User-Settings/updateExtension" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateExtension" class="collapse" aria-labelledby="updateExtension">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#deleteExtension" aria-expanded="true" aria-controls="deleteExtension">Delete Extension</a> 
        
      </td>
      <td class="description"><p>Deletes extension(s) by ID(s).</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>DELETE /restapi/v1.0/account/{accountId}/extension/{extensionId} <a href="https://developers.ringcentral.com/api-reference/User-Settings/deleteExtension" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="deleteExtension" class="collapse" aria-labelledby="deleteExtension">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">savePhoneLines</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">savePhoneNumbers</td>
	      <td class="t">boolean</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readExtensionCallerId" aria-expanded="true" aria-controls="readExtensionCallerId">Get Extension Caller ID</a> 
        
      </td>
      <td class="description"><p>Returns information on an outbound caller ID of an extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-id <a href="https://developers.ringcentral.com/api-reference/User-Settings/readExtensionCallerId" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readExtensionCallerId" class="collapse" aria-labelledby="readExtensionCallerId">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateExtensionCallerId" aria-expanded="true" aria-controls="updateExtensionCallerId">Update Extension Caller ID</a> 
        
      </td>
      <td class="description"><p>Updates outbound caller ID information of an extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-id <a href="https://developers.ringcentral.com/api-reference/User-Settings/updateExtensionCallerId" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateExtensionCallerId" class="collapse" aria-labelledby="updateExtensionCallerId">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#listExtensionGrants" aria-expanded="true" aria-controls="listExtensionGrants">Get Extension Grant List</a> 
        
      </td>
      <td class="description"><p>Returns the list of extensions with the information on grants given to the current extension regarding them. Currently the list of grants include: picking up a call, monitoring, calling or receiving a call on behalf of somebody, call delegation and calling paging groups.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/grant <a href="https://developers.ringcentral.com/api-reference/User-Settings/listExtensionGrants" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="listExtensionGrants" class="collapse" aria-labelledby="listExtensionGrants">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionType</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Type of extension to be returned. Multiple values are supported</td>
            </tr>
<tr>
	      <td class="n">page</td>
	      <td class="t">string</td>
	      <td class="d">1</td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">perPage</td>
	      <td class="t">string</td>
	      <td class="d">100</td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readNotificationSettings" aria-expanded="true" aria-controls="readNotificationSettings">Get Notification Settings</a> 
        
      </td>
      <td class="description"><p>Returns notification settings for the current extension.
 <p>Knowledge Article: <a href="https://success.ringcentral.com/articles/RC_Knowledge_Article/9740">User Settings - Set up Message Notifications</a></p></p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/notification-settings <a href="https://developers.ringcentral.com/api-reference/User-Settings/readNotificationSettings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readNotificationSettings" class="collapse" aria-labelledby="readNotificationSettings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateNotificationSettings" aria-expanded="true" aria-controls="updateNotificationSettings">Update Notification Settings</a> 
        
      </td>
      <td class="description"><p>Updates notification settings for the current extension.
<p>Knowledge Article: <a href="https://success.ringcentral.com/articles/RC_Knowledge_Article/9740">User Settings - Set up Message Notifications</a></p></p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/notification-settings <a href="https://developers.ringcentral.com/api-reference/User-Settings/updateNotificationSettings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateNotificationSettings" class="collapse" aria-labelledby="updateNotificationSettings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">integer</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readUserProfileImage" aria-expanded="true" aria-controls="readUserProfileImage">Get User Profile Image</a> 
        
      </td>
      <td class="description"><p>Returns a profile image of an extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/profile-image <a href="https://developers.ringcentral.com/api-reference/User-Settings/readUserProfileImage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUserProfileImage" class="collapse" aria-labelledby="readUserProfileImage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#createUserProfileImage" aria-expanded="true" aria-controls="createUserProfileImage">Upload User Profile Image</a> 
        
      </td>
      <td class="description"><p>Uploads the extension profile image.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>POST /restapi/v1.0/account/{accountId}/extension/{extensionId}/profile-image <a href="https://developers.ringcentral.com/api-reference/User-Settings/createUserProfileImage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="createUserProfileImage" class="collapse" aria-labelledby="createUserProfileImage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">image</td>
	      <td class="t">file</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateUserProfileImage" aria-expanded="true" aria-controls="updateUserProfileImage">Update User Profile Image</a> 
        
      </td>
      <td class="description"><p>Updates the extension profile image</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/profile-image <a href="https://developers.ringcentral.com/api-reference/User-Settings/updateUserProfileImage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateUserProfileImage" class="collapse" aria-labelledby="updateUserProfileImage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">image</td>
	      <td class="t">file</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de"></td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readScaledPofileImage" aria-expanded="true" aria-controls="readScaledPofileImage">Get Scaled User Profile Image</a> 
        
      </td>
      <td class="description"><p>Returns scaled profile image of an extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/profile-image/{scaleSize} <a href="https://developers.ringcentral.com/api-reference/User-Settings/readScaledPofileImage" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readScaledPofileImage" class="collapse" aria-labelledby="readScaledPofileImage">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">scaleSize</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">Dimensions of a profile image which will be returned in response. If this path parameter is not specified in request URI then</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readConferencingSettings" aria-expanded="true" aria-controls="readConferencingSettings">Get User Conferencing Settings</a> 
        
      </td>
      <td class="description"><p>Returns the information on the Free Conference Calling (FCC) feature for a given extension.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/conferencing <a href="https://developers.ringcentral.com/api-reference/User-Settings/readConferencingSettings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readConferencingSettings" class="collapse" aria-labelledby="readConferencingSettings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">countryId</td>
	      <td class="t">string</td>
	      <td class="d"></td>
	      <td class="r">False</td>
	      <td class="de">Internal identifier of a country. If not specified, the response is returned for the brand country</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateConferencingSettings" aria-expanded="true" aria-controls="updateConferencingSettings">Update User Conferencing Settings</a> 
        
      </td>
      <td class="description"><p>Updates the default conferencing number for the current extension. The number can be selected from conferencing numbers of the current extension. Updates the setting, allowing participants join the conference before host.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/conferencing <a href="https://developers.ringcentral.com/api-reference/User-Settings/updateConferencingSettings" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateConferencingSettings" class="collapse" aria-labelledby="updateConferencingSettings">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de">JSON body</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>

### Video Configuration

<table class="table api-index">
  <thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#readUserVideoConfiguration" aria-expanded="true" aria-controls="readUserVideoConfiguration">Get User Video Configuration</a> 
        
      </td>
      <td class="description"><p>Returns information about video configuration of the current user.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/video-configuration <a href="https://developers.ringcentral.com/api-reference/Video-Configuration/readUserVideoConfiguration" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="readUserVideoConfiguration" class="collapse" aria-labelledby="readUserVideoConfiguration">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the current session account</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
<tr>
      <td class="method">
        
        <a href="#" class="collapsed" data-toggle="collapse" data-target="#updateUserVideoConfiguration" aria-expanded="true" aria-controls="updateUserVideoConfiguration">Update User Video Configuration</a> 
        
      </td>
      <td class="description"><p>Allows to update user video settings, for example video provider.</p></td>
    </tr>
    <tr>
      <td class="endpoint" colspan="2">
        <p>PUT /restapi/v1.0/account/{accountId}/extension/{extensionId}/video-configuration <a href="https://developers.ringcentral.com/api-reference/Video-Configuration/updateUserVideoConfiguration" class="external-link"><i class="fa fa-share"></i></a></p>
	<div id="updateUserVideoConfiguration" class="collapse" aria-labelledby="updateUserVideoConfiguration">

	  <table class="table api-index">
	    <thead>
	      <tr>
	        <th scope="col">Name</th>
		<th scope="col">Type</th>
		<th scope="col">Default</th>
		<th scope="col">Required</th>
		<th scope="col">Description</th>
              </tr>
            </thead>
            <tbody>
<tr>
	      <td class="n">accountId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session</td>
            </tr>
<tr>
	      <td class="n">body</td>
	      <td class="t"></td>
	      <td class="d"></td>
	      <td class="r">True</td>
	      <td class="de"></td>
            </tr>
<tr>
	      <td class="n">extensionId</td>
	      <td class="t">string</td>
	      <td class="d">~</td>
	      <td class="r">True</td>
	      <td class="de">Internal identifier of an extension or tilde (~) to indicate the extension assigned to the current session account</td>
            </tr>
</tbody>
          </table>
</div>
      </td>
    </tr>
</tbody>
</table>
