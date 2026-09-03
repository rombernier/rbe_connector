import time

from sekoia_automation.connector import Connector


# Our connector inherits from the Connector class of the sekoia automation sdk
class RBEConnector(Connector):

    # The run method is called by Sekoia when launching the connector
    def run(self) -> None:
        # The log method is used to trace logs in the Connector logs of the Sekoia interface
        self.log(message="Start fetching events", level="info")
        # Iterate until the Connector is shut down by Sekoia
        while self.running:
            # Complete with your custom code collecting events
            now = int(time.time())
            event1 = 'type="event" subtype="system" level="information" vd="root" logdesc="Admin login successful" sn="1234567890" user="admin" ui="jsconsole" method="jsconsole" srcip=192.0.2.101 dstip=192.0.2.101 action="login" status="success" reason="none" profile="super_admin" msg="Administrator admin logged in successfully from jsconsole"'
            event2 = f'CEF:0|Fortinet|Fortigate|v6.0.4|32021|event:system login failed|7|deviceExternalId=FGVM2V0000171868 FortinetFortiGatelogid=0100032021 cat=event:system FortinetFortiGatesubtype=system FortinetFortiGatelevel=alert FortinetFortiGatevd=root FortinetFortiGateeventtime={now} FortinetFortiGatelogdesc=Admin login disabled sproc=192.0.2.101 FortinetFortiGateaction=login outcome=failed reason=exceed_limit msg=Login disabled from IP 192.0.2.101 for 60 seconds because of 3 bad attempts'
            event3 = f'logver=60 timestamp={now} tz="UTC+2" devname="abc" devid="1" vd="IPSEC" date=2019-08-27 time=16:27:40 logid="0101039949" type="event" subtype="vpn" level="information" eventtime={now} logdesc="SSL VPN statistics" action="tunnel-stats" tunneltype="ssl-tunnel" tunnelid=1995 remip=192.0.2.101 tunnelip=192.0.2.1 user="test" group="GRP_Generic_JAIL_VPN" dst_host="N/A" nextstat=600 duration=8437 sentbyte=71524041 rcvdbyte=6151809 msg="SSL tunnel statistics"'
            

            # Ingest the collected events in Sekoia
            batch_of_events = [event1, event2, event3]
            if len(batch_of_events) > 0:
                self.log(
                    message=f"{len(batch_of_events)} events collected",
                    level="info",
                )
                self.push_events_to_intakes(events=batch_of_events)
                self.log(message="Events pushed to intakes!", level="info")
            # Wait 60s before collecting the next batch of events
            time.sleep(60)
