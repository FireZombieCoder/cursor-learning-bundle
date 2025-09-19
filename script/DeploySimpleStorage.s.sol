// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Script.sol";
import "../contracts/stage0/SimpleStorage.sol";

/**
 * @title DeploySimpleStorage
 * @dev Deployment script for the SimpleStorage contract
 * @author Base Learning Curriculum
 */
contract DeploySimpleStorage is Script {
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        address deployer = vm.addr(deployerPrivateKey);

        console.log("Deploying contracts with account:", deployer);
        console.log("Account balance:", deployer.balance);

        vm.startBroadcast(deployerPrivateKey);

        SimpleStorage simpleStorage = new SimpleStorage();

        vm.stopBroadcast();

        console.log("SimpleStorage deployed to:", address(simpleStorage));
        console.log("Contract owner:", simpleStorage.owner());
        console.log("Initial stored data:", simpleStorage.storedData());
        console.log("Initial stored string:", simpleStorage.storedString());
    }
}
