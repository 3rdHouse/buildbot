    @defer.inlineCallbacks
    def run_vc(self, branch, revision, patch):
        self.stdio_log = yield self.addLogForRemoteCommands("stdio")
            yield self.patch(patch)
        return SUCCESS