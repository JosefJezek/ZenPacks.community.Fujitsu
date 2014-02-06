
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }

    ZC.FujitsuLogicalDiskPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'FujitsuLogicalDisk',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "arraySize"
                    }, 
                    {
                        "name": "cacheMode"
                    }, 
                    {
                        "name": "getRaidStatus"
                    }, 
                    {
                        "name": "osName"
                    }, 
                    {
                        "name": "raidLevel"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "header": "Array Size GB", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "arraySize", 
                        "dataIndex": "arraySize"
                    }, 
                    {
                        "header": "Cache Mode", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "cacheMode", 
                        "dataIndex": "cacheMode"
                    }, 
                    {
                        "header": "RAID Status", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getRaidStatus", 
                        "dataIndex": "getRaidStatus"
                    }, 
                    {
                        "header": "OS Name", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "osName", 
                        "dataIndex": "osName"
                    }, 
                    {
                        "header": "RAID Level", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "raidLevel", 
                        "dataIndex": "raidLevel"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.FujitsuLogicalDiskPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('FujitsuLogicalDiskPanel', ZC.FujitsuLogicalDiskPanel);
    ZC.registerName('FujitsuLogicalDisk', _t('Logical Disk'), _t('Logical Disks'));
    
    })();

